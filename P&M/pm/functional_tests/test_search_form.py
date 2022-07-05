from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

import time
import unittest


class SearchFormTest(FunctionalTest, unittest.TestCase):
    MAX_WAIT = 10

    def wait_for_string(self, expected_string, setting, setting_name):
        start_time = time.time()
        while True:
            try:
                info = self.browser.find_element(setting, setting_name)
                self.assertIn(expected_string, info.text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    return e
                return time.sleep(0.5)

    def test_search_form_excist_medcine(self):
        self.browser.get('http://127.0.0.1:8000/')

        input_box = self.browser.find_element(By.ID, 'search')
        self.assertEqual('Введите название препарата', input_box.get_attribute('placeholder'))

        input_box.send_keys('Ибуфен')
        input_box.send_keys(Keys.ENTER)

        self.wait_for_string('ИБУФЕН', By.ID, 'info')

    def test_search_form_not_excist_medcine(self):
        self.browser.get('http://127.0.0.1:8000/')

        input_box = self.browser.find_element(By.ID, 'search')

        input_box.send_keys('sfggd')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_string('Препарата нет в базе данных', By.TAG_NAME, 'p')
