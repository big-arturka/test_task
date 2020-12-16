from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from news_client.models import Category


class NotAuthCategoryListTestCase(TestCase):
    def test_open_index(self):
        response = self.client.get(reverse('news_client:category_list'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthCategoryCreateTestCase(TestCase):
    def test_get_create_article(self):
        response = self.client.get(reverse('news_client:category_create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_create_article(self):
        response = self.client.post(reverse('news_client:category_create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthCategoryUpdateTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='category')

    def test_get_update_article(self):
        response = self.client.get(reverse('news_client:category_update', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_update_article(self):
        response = self.client.post(reverse('news_client:category_update', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthCategoryDeleteTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title='category')

    def test_get_update_article(self):
        response = self.client.get(reverse('news_client:category_delete', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_update_article(self):
        response = self.client.post(reverse('news_client:category_delete', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))
