import unittest
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
import time


class FunctionalTest(LiveServerTestCase):
    MAX_WAIT = 10

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        # staging_server = os.environ.get('STAGING_SERVER')
        # if staging_server:
        #     self.live_server_url = 'http://' + staging_server

    def tearDown(self) -> None:
        self.browser.quit()

    @staticmethod
    def wait(fn):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            while True:
                try:
                    return fn(*args, **kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > FunctionalTest.MAX_WAIT:
                        return e
                    return time.sleep(0.5)

        return wrapper

    @wait
    def wait_for_string(self, fn):
        return fn()

    def get_search_form(self):
        return self.browser.find_element(By.ID, 'search')
