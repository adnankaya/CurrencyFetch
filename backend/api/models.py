from django.db import models

from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True
        default_manager_name = "objects"


class BaseImage(Base):
    class Status(models.TextChoices):
        ACTIVE = "A", _("Active")
        PASSIVE = "P", _("Passive")

    status = models.CharField(
        max_length=1, choices=Status.choices, default=Status.ACTIVE
    )

    class Meta:
        abstract = True
        ordering = ("order",)


class Currency(Base):
    slug = models.SlugField(max_length=64, unique=True)
    symbol = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=128, unique=True)
    last_updated = models.DateTimeField()
    is_crypto = models.BooleanField(default=True)

    class Meta:
        db_table = "t_currency"
    
    def __str__(self) -> str:
        return self.slug


class CurrencyImage(BaseImage):
    small = models.CharField(max_length=1024, null=True, blank=True)
    thumb = models.CharField(max_length=1024, null=True, blank=True)
    large = models.CharField(max_length=1024, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_currency_image"


class CurrencyPrice(Base):
    default_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="default_currency_prices"
    )
    vs_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="vs_currency_prices"
    )
    price = models.DecimalField(max_digits=64, decimal_places=12)

    class Meta:
        db_table = "t_currency_price"
    
    def __str__(self) -> str:
        return f"{self.default_currency.symbol}/{self.vs_currency.symbol} : {self.price}"
