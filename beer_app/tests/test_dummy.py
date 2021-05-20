from django.test import TestCase, SimpleTestCase

# Create your tests here.

class DummyTestCase(SimpleTestCase):

    def test_dummy(self):
        self.assertTrue(True)