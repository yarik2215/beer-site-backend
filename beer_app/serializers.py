from rest_framework import serializers

from .models import Beer, UserComment


class BeerSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField()

    class Meta:
        model = Beer
        fields = '__all__'


class BeerListSerializer(BeerSerializer):

    class Meta:
        model = Beer
        fields = ['id', 'name', 'price', 'mark', 'updated_at', 'image', 'rating']

    # def get_averrage_mark(self):
    #     pass

