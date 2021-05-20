from django.test import TestCase
from django.urls import reverse

from beer_app.models import Beer, UserComment


class BeerApiTestCase(TestCase):

    def setUp(self) -> None:
        
        Beer.objects.create(
            name='beer_1',
            mark=5,
            price=25.1
        )

    def test_retrieve_beer_list_200_ok(self):
        response = self.client.get(reverse('beer-app:beer-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)

    def test_retirieve_beer_200_ok(self):
        response = self.client.get(reverse('beer-app:beer-detail', args=[1]))
        self.assertEqual(response.status_code, 200)
