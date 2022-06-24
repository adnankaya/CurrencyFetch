from typing import Any, Optional
from django.core.management.base import BaseCommand
from django.db import transaction
from django.db import IntegrityError
from django.db.transaction import TransactionManagementError
from django.utils import timezone
import random
import decimal
import datetime
import requests
import json

# internal
from api.models import Currency, CurrencyImage, CurrencyPrice


class Command(BaseCommand):
    help = "Fetches the data from external api to store in database"

    API_URL = "https://api.coingecko.com/api/v3/coins/"

    ALL_COINS_DATA = None

    def fetch_coins(self):
        try:
            response = requests.get(self.API_URL)
            return response.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"ERROR...\n{e}"))

    def import_world_currencies(self):
        with open("world-currencies.json", "r") as f:
            currency_data = json.load(f)

        for currency in currency_data:
            try:
                Currency.objects.create(
                    slug=currency.get("code").lower(),
                    symbol=currency.get("code").lower(),
                    name=currency.get("name"),
                    last_updated=timezone.now(),
                    is_crypto=False,
                )

            except IntegrityError:
                pass
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"import_world_currencies:ERROR...\n{e}"))

    def create_currency_data(self):
        self.ALL_COINS_DATA = self.fetch_coins()
        self.import_world_currencies()

        with transaction.atomic():
            for coin_data in self.ALL_COINS_DATA:
                try:
                    slug = coin_data.get("id")
                    default_symbol = coin_data.get("symbol")
                    name = coin_data.get("name")
                    last_updated = coin_data.get("last_updated")

                    currency = Currency(
                        slug=slug,
                        symbol=default_symbol,
                        name=name,
                        last_updated=last_updated,
                    )
                    currency.save()

                    CurrencyImage.objects.create(
                        currency=currency, **coin_data.get("image")
                    )

                except IntegrityError:
                    pass
                except TransactionManagementError:
                    pass
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"create_currency_data:ERROR...\n{e}")
                    )

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write(self.style.SUCCESS("Process started..."))
        # first create coins
        self.create_currency_data()

        with transaction.atomic():
            try:
                for coin_data in self.ALL_COINS_DATA:
                    slug = coin_data.get("id")
                    currency = Currency.objects.get(slug=slug)
                    coin_price_data = (
                        coin_data.get("market_data").get("current_price").items()
                    )

                    for symbol, price in coin_price_data:
                        try:
                            vs_currency = Currency.objects.get(symbol=symbol)
                            currency_price = CurrencyPrice(
                                default_currency=currency,
                                vs_currency=vs_currency,
                                price=price,
                            )
                            currency_price.save()
                        except Currency.DoesNotExist:
                            continue

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"handle:ERROR...\n{e}"))

        self.stdout.write(self.style.SUCCESS("Process finished..."))
