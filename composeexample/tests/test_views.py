from django.test import TestCase
from django.test.client import Client


class TestIndexView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'the index page', response.content)
