from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse
from news_client.models import Article, Category


class AuthIndexTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_open_index(self):
        response = self.client.get(reverse('news_client:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthArticleDetailTestCase(TestCase):
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

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_open_article(self):
        response = self.client.get(reverse('news_client:article_view', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthArticleCreateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='add_article')
        cls.user.user_permissions.add(permission)
        cls.category = Category.objects.create(title='category')

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_create_article_success(self):
        response = self.client.get(reverse('news_client:article_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_create_article_success(self):
        url = reverse('news_client:article_create')
        data = {'title': 'test title', 'description': 'test description', 'category_id': self.category.pk}
        response = self.client.post(url, data)
        article = Article.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:article_view', kwargs={'pk': article.pk})
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.description, data['description'])
        self.assertEqual(article.user_id, self.user)
        self.assertEqual(article.category_id, self.category)


class AuthArticleUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='change_article')
        cls.user.user_permissions.add(permission)
        cls.category = Category.objects.create(title='category')
        cls.article = Article.objects.create(title='test title', category_id=cls.category, description='description',
                                             user_id=cls.user)

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_create_update_success(self):
        response = self.client.get(reverse('news_client:article_update', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_create_update_success(self):
        url = reverse('news_client:article_update', kwargs={'pk': self.article.pk})
        data = {'title': 'test title', 'description': 'test description', 'category_id': self.category.pk}
        response = self.client.post(url, data)
        article = Article.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:article_view', kwargs={'pk': article.pk})
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.description, data['description'])
        self.assertEqual(article.user_id, self.user)
        self.assertEqual(article.category_id, self.category)


class AuthArticleDeleteTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='delete_article')
        cls.user.user_permissions.add(permission)
        cls.category = Category.objects.create(title='category')
        cls.article = Article.objects.create(title='test title', category_id=cls.category, description='description',
                                             user_id=cls.user)

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_delete_article_success(self):
        response = self.client.get(reverse('news_client:article_delete', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_delete_article_success(self):
        url = reverse('news_client:article_delete', kwargs={'pk': self.article.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:index')
        self.assertEqual(response.url, redirect_url)
