from django.contrib.auth import get_user_model
from django.db.models import Model
from django.test import TestCase
from accounts.forms import MyUserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm


class UserCreationFormTestCase(TestCase):
    def test_form_success(self):
        form = MyUserCreationForm(data={'username': 'user', 'password1': 'user', 'password2': 'user'})
        self.assertTrue(form.is_valid())

    def test_form_error_not_required_fields(self):
        form = MyUserCreationForm(data={'username': 'user', 'password1': 'user'})
        self.assertFalse(form.is_valid())

    def test_form_error_passwords_do_not_match(self):
        form = MyUserCreationForm(data={'username': 'user', 'password1': 'user', 'password2': 'other password'})
        self.assertFalse(form.is_valid())


class UserChangeFormTestCase(TestCase):
    def test_form_success(self):
        form = UserChangeForm(data={'first_name': 'test', 'last_name': 'test', 'email': 'email@email.com'})
        self.assertTrue(form.is_valid())

    def test_form_email_field_error(self):
        form = UserChangeForm(data={'email': 'email'})
        self.assertFalse(form.is_valid())


class SetPasswordFormTestCase(TestCase):
    def test_form_success(self):
        form = SetPasswordForm(data={'password': 'user', 'password_confirm': 'user'})
        self.assertTrue(form.is_valid())

    def test_form_error_passwords_do_not_match(self):
        form = SetPasswordForm(data={'password': 'user', 'password_confirm': 'other'})
        self.assertFalse(form.is_valid())

    def test_form_error_not_required_fields(self):
        form = SetPasswordForm(data={'password': 'user'})
        self.assertFalse(form.is_valid())


class PasswordChangeFormTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_form_password_success(self):
        self.assertTrue(self.user.check_password('admin'))

    def test_form_password_incorrect(self):
        self.assertFalse(self.user.check_password('other'))

    def test_form_error_not_required_fields(self):
        form = PasswordChangeForm(data={})
        self.assertFalse(form.is_valid())