from rest_framework import serializers

from .models import Currency, CurrencyImage, CurrencyPrice


class CurrencyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyImage
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    currencyimage_set = CurrencyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Currency
        fields = "__all__"


class CurrencyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyPrice
        fields = "__all__"


class DefaultCurrencyPriceSerializer(serializers.ModelSerializer):
    vs_currency_slug = serializers.ReadOnlyField(source="vs_currency.slug")

    class Meta:
        model = CurrencyPrice
        fields = ("price", "vs_currency", "default_currency", "vs_currency_slug")


class CurrencyDetailedSerializer(serializers.ModelSerializer):
    currencyimage_set = CurrencyImageSerializer(many=True, read_only=True)
    # default_currency_prices = DefaultCurrencyPriceSerializer(many=True, read_only=True)
    price = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = (
            "id",
            "name",
            "slug",
            "symbol",
            "price",
            "created_date",
            "updated_date",
            "last_updated",
            "currencyimage_set",
            # "default_currency_prices",
        )

    def get_price(self, instance):
        usd = Currency.objects.get(symbol="usd")
        cp = (
            instance.default_currency_prices.filter(vs_currency=usd)
            .order_by("-created_date")
            .first()
        )
        if cp:
            return cp.price
