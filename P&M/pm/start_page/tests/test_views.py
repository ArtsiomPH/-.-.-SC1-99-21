import unittest

import start_page
from start_page.views import *
from django.http import HttpRequest
from django.test import TestCase
from start_page.forms import Search, Add_medcine
from django.utils.html import escape
from unittest.mock import patch, Mock

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


class IsoTest(unittest.TestCase):

    def setUp(self) -> None:
        self.request = HttpRequest()

    @patch('start_page.views.render')
    def test_start_page_render(self, mock_render):
        response = index(self.request)
        self.assertEqual(response, mock_render.return_value)




