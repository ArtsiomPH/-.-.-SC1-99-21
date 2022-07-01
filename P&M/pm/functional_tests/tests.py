from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import time
import unittest

from start_page.models import Medcine


class NewVisitorTest(LiveServerTestCase):
    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_string(self, expected_string):
        start_time = time.time()
        while True:
            try:
                info = self.browser.find_element(By.TAG_NAME, 'p')
                self.assertIn(expected_string, info.text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    return e
                return time.sleep(0.5)

    def test_start_page(self):
        self.browser.get(self.live_server_url)

        self.assertIn('P&M', self.browser.title)

        headers_text = self.browser.find_elements(By.TAG_NAME, 'h4')
        self.assertIn('Новые препараты', [text.text for text in headers_text])

    def test_search_form_not_excist_medcine(self):
        self.browser.get(self.live_server_url)

        input_box = self.browser.find_element(By.ID, 'search')
        self.assertEqual('Введите название препарата', input_box.get_attribute('placeholder'))

        input_box.send_keys('sfggd')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_string('Препарата нет в базе данных')



    def test_layout(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        infobox = self.browser.find_element(By.ID, 'new')
        self.assertAlmostEqual(infobox.location['x'] + infobox.size['width']/2,
                               512,
                               delta=10
        )

        self.fail("End test")
class SearchFormTest(unittest.TestCase):
    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_string(self, expected_string, settings, settings_name):
        start_time = time.time()
        while True:
            try:
                info = self.browser.find_element(settings, settings_name)
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

# if __name__ == '__main__':
#     unittest.main()
