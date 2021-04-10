import django_filters

from django_filters import NumberFilter, CharFilter

from .models import *

class ProductFilter(django_filters.FilterSet):
    # price_filter = NumberFilter(field_name="price", lookup_expr='lt')
    # name_filter = CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['productCode', 'description', 'date_created', 'price', 'name']
        exclude = ['productCode', 'description', 'date_created']

