from django.db.models import Avg, FloatField
from django.db.models.functions import Coalesce
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet

from .models import Beer
from .serializers import BeerListSerializer, BeerSerializer
from .filters import BeerFilter


class BeerViewset(ModelViewSet):
    queryset = Beer.objects.all().annotate(rating=Coalesce(Avg('user_comments__mark'), 0, output_field=FloatField()))
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = BeerFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return BeerListSerializer
        return BeerSerializer
