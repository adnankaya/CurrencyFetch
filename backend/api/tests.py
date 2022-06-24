from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import random
from django.utils import timezone

# internals
from .models import Currency, CurrencyPrice


class BaseTestCase(TestCase):
    url_api_prefix = "/api/v1/"

    def setUp(self) -> None:
        self.client = APIClient()


class CurrencyViewsetTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.last_updated = timezone.now()
        self.curr_usd = Currency.objects.create(
            slug="usd",
            symbol="usd",
            name="United States Dollar",
            last_updated=self.last_updated,
        )
        self.curr_btc = Currency.objects.create(
            slug="bitcoin", symbol="btc", name="Bitcoin", last_updated=self.last_updated
        )
        self.curr_eth = Currency.objects.create(
            slug="ethereum",
            symbol="eth",
            name="Ethereum",
            last_updated=self.last_updated,
        )

        CurrencyPrice.objects.create(
            default_currency=self.curr_btc,
            vs_currency=self.curr_usd,
            price=Decimal("32456"),
        )
        CurrencyPrice.objects.create(
            default_currency=self.curr_eth,
            vs_currency=self.curr_usd,
            price=Decimal("21456"),
        )

    def test_list_currencies(self):
        endpoint = f"{self.url_api_prefix}currencies/"
        res = self.client.get(endpoint)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        res_data = res.json()
        self.assertEqual(res_data.get("count"), 3)
        self.assertEqual(res_data.get("current_page"), 1)
        self.assertEqual(res_data.get("total_pages"), 1)
        for curr in res_data.get("results"):
            if curr.get("symbol") == "btc":
                self.assertEqual(
                    Decimal(curr.get("price")),
                    self.curr_btc.default_currency_prices.first().price,
                )

    def test_post_currency(self):
        name = "Currency"
        symbol = "curr"
        slug = "curr"
        last_updated = self.last_updated
        payload = {
            "name": name,
            "symbol": symbol,
            "slug": slug,
            "last_updated": last_updated,
        }
        endpoint = f"{self.url_api_prefix}currencies/"
        res = self.client.post(endpoint, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res_data = res.json()
        self.assertEqual(res_data.get("name"), name)
        self.assertEqual(res_data.get("symbol"), symbol)
        self.assertEqual(res_data.get("slug"), slug)
        self.assertEqual(
            res_data.get("last_updated"), last_updated.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        )

    def test_post_currency_price(self):
        price = Decimal("12345")
        payload = {
            "price": price,
            "default_currency": self.curr_usd.id,
            "vs_currency": self.curr_btc.id,
        }
        endpoint = f"{self.url_api_prefix}currency-prices/"
        res = self.client.post(endpoint, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        res_data = res.json()
        self.assertEqual(Decimal(res_data.get("price")), price)
