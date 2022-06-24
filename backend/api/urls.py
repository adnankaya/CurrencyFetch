from rest_framework import routers
from django.urls import path, include


# internals
from . import views


router = routers.DefaultRouter()

router.register('currencies', views.CurrencyViewset)
router.register('currency-prices', views.CurrencyPriceViewset)
router.register('currency-images', views.CurrencyImageViewset)


urlpatterns = [
    path('hi/', views.hi),
    path('', include(router.urls))
]
