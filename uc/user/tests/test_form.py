from django.test import TestCase
from user.forms import RegisterForm


class UserFormTests(TestCase):

    def test_register_invalid(self):
        form = RegisterForm()
        self.assertFalse(form.is_valid())

    def test_register_empty(self):
        form = RegisterForm(data={'username': "", 'password': "", 'confirm_password': ""})
        self.assertFalse(form.is_valid())

    def test_register_wrong_password(self):
        form = RegisterForm(data={'username': "test_user", 'password': "pass_word", 'confirm_password': "pass"})
        self.assertFalse(form.is_valid())

    def test_register_ok(self):
        form = RegisterForm(data={'username': "test_user", 'password': "pass_word_123", 'confirm_password': "pass_word_123"})
        self.assertTrue(form.is_valid())
