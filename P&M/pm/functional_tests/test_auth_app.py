import time


from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase, LiveServerTestCase
from django.core import mail
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore

from .base import FunctionalTest
import unittest

TEST_EMAIL = 'edith@example.com'
SUBJECT = 'Your login link for Superlists'
User = get_user_model()


class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_log_in(self):
        # self.browser.get('http://127.0.0.1:8000/auth/login/')
        #
        # self.browser.find_element(By.TAG_NAME, 'button').click()
        # self.wait_for_string(lambda: self.assertIn('Поле обязательно', self.browser.find_element(By.CSS_SELECTOR,

        self.create_pre_auth_session(username='ok', password='ok')

        self.browser.get(self.live_server_url)

        self.assertEqual(self.browser.find_element(By.ID, 'base').text, 'База данных')
        # self.browser.get('http://127.0.0.1:8000/auth/password_reset/')
        #
        # self.browser.find_element(By.NAME, 'email').send_keys('tema092009@mail.ru').send_keys(Keys.ENTER)
        #
        # email = mail.outbox[0]
        # self.assertIn('tema092009@mail.ru', email.to)
        # self.assertEqual(email.subject, SUBJECT)
        #
        # self.assertIn('Use this link to log in', email.body)
        # url_search = re.search(r'http://.+/.+$', email.body)
        # if not url_search:
        #     self.fail(f'Could not find url in email body:\n{email.body}')
        # url = url_search.group(0)
        # self.assertIn(self.live_server_url, url)
        #
        # self.browser.get(url)
        #
        # # self.wait_for_string('Log out', By.LINK_TEXT)
        #
        # navbar = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        # self.assertIn(TEST_EMAIL, navbar.text)

    def create_pre_auth_session(self, username, password):
        user = User.objects.create(username=username, password=password)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.create()
        self.browser.get(self.live_server_url + "/404/")
        self.browser.add_cookie(dict(name=settings.SESSION_COOKIE_NAME, value=session.session_key, path='/',))
