from rest_framework import viewsets, mixins

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

# internals
from .serializers import (
    CurrencyDetailedSerializer,
    CurrencyPriceSerializer,
    CurrencySerializer,
    CurrencyImageSerializer,
)
from .models import Currency, CurrencyImage, CurrencyPrice
from .pagination import BasePageNumberPagination


@api_view()
def hi(request):
    return Response({"message": "Hello, world!"})


class BaseViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CurrencyViewset(BaseViewset):
    pagination_class = BasePageNumberPagination
    serializer_class = CurrencyDetailedSerializer
    queryset = Currency.objects.filter(is_crypto=True).order_by('created_date')

    def get_queryset(self):
        query = self.request.query_params.get("query")
        if query:
            qobj = (
                Q(slug__istartswith=query)
                | Q(symbol__istartswith=query)
                | Q(name__istartswith=query)
            )
            return self.queryset.filter(qobj)
        return self.queryset.order_by('created_date')


class CurrencyImageViewset(BaseViewset):
    pagination_class = BasePageNumberPagination
    serializer_class = CurrencyImageSerializer
    queryset = CurrencyImage.objects.all()


class CurrencyPriceViewset(BaseViewset):
    pagination_class = BasePageNumberPagination
    serializer_class = CurrencyPriceSerializer
    queryset = CurrencyPrice.objects.all().order_by('-created_date')

    def get_queryset(self):
        vs = self.request.query_params.get("vs")
        default = self.request.query_params.get("dc")
        if vs and default:
            try:
                vs_currency = Currency.objects.get(symbol=vs)
                default_currency = Currency.objects.get(symbol=default)
                qset = self.queryset.filter(
                    vs_currency=vs_currency, default_currency=default_currency
                ).order_by("-created_date")
                return qset
            except Currency.DoesNotExist:
                return self.queryset
        return self.queryset
