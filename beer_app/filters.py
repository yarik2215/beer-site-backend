from django_filters import rest_framework as rest_filters
from django_filters import filters


class BeerFilter(rest_filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_mark = filters.NumberFilter(field_name="mark", lookup_expr='gte')
    max_mark = filters.NumberFilter(field_name="mark", lookup_expr='lte')
    min_rating = filters.NumberFilter(field_name="rating", lookup_expr='gte')
    max_rating = filters.NumberFilter(field_name="rating", lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    order = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('mark', 'mark'),
            ('rating', 'rating'),
            ('updated_at', 'updated_at'),
        )
    )

