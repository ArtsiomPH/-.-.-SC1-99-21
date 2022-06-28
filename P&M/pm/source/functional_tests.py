from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_start_page(self):
        self.browser.get('http://localhost:8000/')

        self.assertIn('P&M', self.browser.title)
        # self.fail("End test")


if __name__ == '__main__':
    unittest.main()
