from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import views


beer_router = DefaultRouter()
beer_router.register(r'beers', views.BeerViewset)

app_name = 'beer-app'
urlpatterns = [
    path('', include(beer_router.urls))
]