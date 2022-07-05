from django.test import TestCase
from start_page.forms import Search, Add_medcine
from django.utils.html import escape

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

    def test_start_page_uses_search_form(self):
        response = self.client.get("/")
        self.assertIsInstance(response.context["form"], Search)

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.get("/base/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'start_page/base_operations.html')


