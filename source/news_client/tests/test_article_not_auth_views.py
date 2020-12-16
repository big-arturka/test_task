from django.contrib.auth import get_user_model
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser
from news_client.models import Article, Category


class NotAuthIndexTestCase(TestCase):
    def test_open_index(self):
        response = self.client.get(reverse('news_client:index'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthArticleDetailTestCase(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(username='admin', password='admin')
        self.category = Category.objects.create(title='category')
        self.article = Article.objects.create(title='test title', category_id=self.category,
                                              description='description', user_id=self.user)

    def test_open_article(self):
        response = self.client.get(reverse('news_client:article_view', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthArticleCreateTestCase(TestCase):
    def test_get_create_article(self):
        response = self.client.get(reverse('news_client:article_create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_create_article(self):
        response = self.client.post(reverse('news_client:article_create'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthArticleUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        cls.category = Category.objects.create(title='category')
        cls.article = Article.objects.create(title='test title', category_id=cls.category, description='description',
                                             user_id=cls.user)

    def test_get_update_article(self):
        response = self.client.get(reverse('news_client:article_update', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_update_article(self):
        response = self.client.post(reverse('news_client:article_update', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))


class NotAuthArticleDeleteTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        cls.category = Category.objects.create(title='category')
        cls.article = Article.objects.create(title='test title', category_id=cls.category, description='description',
                                             user_id=cls.user)

    def test_get_delete_article(self):
        response = self.client.get(reverse('news_client:article_delete', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))

    def test_post_delete_article(self):
        response = self.client.post(reverse('news_client:article_delete', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        url, next = response.url.split('?')
        self.assertEqual(url, reverse('accounts:login'))
