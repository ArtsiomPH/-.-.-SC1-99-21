from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_start_page(self):
        self.browser.get(self.live_server_url)

        self.assertIn('P&M', self.browser.title)

        headers_text = self.browser.find_elements(By.TAG_NAME, 'h4')
        self.assertIn('Новые препараты', [text.text for text in headers_text])

    def test_layout(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        infobox = self.browser.find_element(By.ID, 'new')
        self.assertAlmostEqual(infobox.location['x'] + infobox.size['width'] / 2,
                               512,
                               delta=10
                               )