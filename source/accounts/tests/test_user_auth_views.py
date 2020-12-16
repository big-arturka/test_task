from django.contrib.auth import get_user_model
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse


class AuthDetailViewTestCase(TestCase):
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

    def test_user_detail(self):
        response = self.client.get(reverse('accounts:detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthUsersListTestCase(TestCase):
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

    def test_user_list(self):
        response = self.client.get(reverse('accounts:list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthUserChangeTestCase(TestCase):
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

    def test_get_user_change(self):
        response = self.client.get(reverse('accounts:change', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_user_change(self):
        data = {"first_name": "rabotay", "last_name": "suka", "email": "suka"}
        response = self.client.post(reverse('accounts:change', kwargs={'pk': self.user.pk}), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthPasswordChangeTestCase(TestCase):
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

    def test_get_password_change(self):
        response = self.client.get(reverse('accounts:password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_password_change(self):
        data = {'password': 'admin1', 'password_confirm': 'admin1', 'old_password': 'admin'}
        response = self.client.post(reverse('accounts:password_change'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        response_url = response.url.split('?')
        self.assertEqual(response_url[0], reverse('accounts:detail', kwargs={'pk': self.user.pk}))


class AuthUserDeleteTestCase(TestCase):
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

    def test_get_user_delete(self):
        response = self.client.get(reverse('accounts:delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_user_delete(self):
        response = self.client.post(reverse('accounts:delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        response_url = response.url.split('?')
        self.assertEqual(response_url[0], reverse('news_client:index'))