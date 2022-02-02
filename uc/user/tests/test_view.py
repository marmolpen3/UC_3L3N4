from rest_framework.test import APIClient, APITestCase
from django.urls.base import reverse
from django.contrib.auth.models import User


class RegisterTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def tearDown(self):
        self.client = None

    def test_register_user_wrong_password(self):
        response = self.client.post(reverse('user_register'), data={'username': "test_user", 'password': "pass_word_123", 'confirm_password': "pass_word"})
        self.assertTrue(response.context['error'])

    def test_register_user_duplicate(self):
        self.client.post(reverse('user_register'), data={'username': "test_user", 'password': "pass_word_123", 'confirm_password': "pass_word_123"})
        response = self.client.post(reverse('user_register'), data={'username': "test_user", 'password': "pass_word_123", 'confirm_password': "pass_word_123"})
        self.assertTrue(response.context['error'])

    def test_register_user_ok(self):
        self.client.post(reverse('user_register'), data={'username': "test_user", 'password': "pass_word_123", 'confirm_password': "pass_word_123"})
        user = User.objects.get(username="test_user")
        self.assertEqual(user.username, "test_user")
