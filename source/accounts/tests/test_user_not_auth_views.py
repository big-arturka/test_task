from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser


class NotAuthRegisterTestCase(TestCase):
    def test_get_register_form(self):
        response = self.client.get(reverse('accounts:create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        response_url = response.url.split('?')
        self.assertEqual(response_url[0], reverse('accounts:login'))


class NotAuthDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='admin', password='admin')

    def test_user_detail(self):
        response = self.client.get(reverse('accounts:detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthUsersListTestCase(TestCase):
    def test_user_list(self):
        response = self.client.get(reverse('accounts:list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthUserChangeTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='admin', password='admin')

    def test_user_change(self):
        response = self.client.get(reverse('accounts:change', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthUserDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='admin', password='admin')

    def test_get_user_detail(self):
        response = self.client.get(reverse('accounts:delete', kwargs={'pk': self.user.pk}))
        self.make_assert(response)

    def test_post_user_detail(self):
        response = self.client.post(reverse('accounts:delete', kwargs={'pk': self.user.pk}))
        self.make_assert(response)

    def make_assert(self, response):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))