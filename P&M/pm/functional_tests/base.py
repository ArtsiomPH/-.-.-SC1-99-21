from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest:
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        # staging_server = os.environ.get('STAGING_SERVER')
        # if staging_server:
        #     self.live_server_url = 'http://' + staging_server

    def tearDown(self) -> None:
        self.browser.quit()

    def get_search_form(self):
        return self.browser.find_element(By.ID, 'search')