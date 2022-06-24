from django.contrib import admin

# Register your models here.
from .models import Currency, CurrencyPrice


admin.site.register([Currency, CurrencyPrice])
