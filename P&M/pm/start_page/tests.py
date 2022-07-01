from django.test import TestCase
from .models import Medcine, Synonyms


class HomePageTest(TestCase):
    def test_uses_start_page(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, 'start_page/start.html')

    def test_uses_error(self):
        response = self.client.get("/error/")
        self.assertTemplateUsed(response, 'start_page/not_in_base.html')

    def test_redirect_error(self):
        response = self.client.get("/search/", {"medcine_name": "ssss"})
        self.assertRedirects(response, '/error/')




