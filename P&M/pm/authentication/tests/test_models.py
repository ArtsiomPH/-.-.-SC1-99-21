from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):

    def test_user_is_valid(self):
        user = User(username='name', password='password')
        self.assertFalse(user.is_staff)

