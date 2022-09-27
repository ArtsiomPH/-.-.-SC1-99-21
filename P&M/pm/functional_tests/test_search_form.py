import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest
from start_page.models import Synonyms, Medcine

import unittest


class SearchFormTest(FunctionalTest):
    def test_search_form_excist_medcine(self):
        self.browser.get('http://127.0.0.1:8000/')

        input_box = self.get_search_form()
        self.assertEqual('Введите название препарата', input_box.get_attribute('placeholder'))

        input_box.send_keys('Ибуфен')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_string(lambda: self.assertIn("ИБУФЕН", self.browser.find_element(By.ID, 'info').text))

    def test_search_form_not_excist_medcine(self):
        self.browser.get(self.live_server_url)

        input_box = self.get_search_form()

        input_box.send_keys('sfggd')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_string(lambda: self.assertIn('Препарата нет в базе данных', self.browser.find_element(By.TAG_NAME,
                                                                                                            'p').text))

    def test_cannot_add_empty_item(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.TAG_NAME, "button").click()

        self.wait_for_string(lambda: self.assertEqual("nvghjjdhg", self.browser.find_element(By.CSS_SELECTOR,
                                                                                             '.has-error').text))
