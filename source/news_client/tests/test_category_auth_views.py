from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.template import TemplateDoesNotExist
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse
from news_client.models import Category


class AuthCategoryListTestCase(TestCase):
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

    def test_open_category_list(self):
        response = self.client.get(reverse('news_client:category_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)


class AuthCategoryCreateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='add_category')
        cls.user.user_permissions.add(permission)

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_category_success(self):
        response = self.client.get(reverse('news_client:category_create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_category_success(self):
        url = reverse('news_client:category_create')
        data = {'title': 'test title'}
        response = self.client.post(url, data)
        category = Category.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:category_list')
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(category.title, data['title'])


class AuthCategoryUpdateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='change_category')
        cls.user.user_permissions.add(permission)
        cls.category = Category.objects.create(title='category')

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_update_category_success(self):
        response = self.client.get(reverse('news_client:category_update', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_post_update_category_success(self):
        url = reverse('news_client:category_update', kwargs={'pk': self.category.pk})
        data = {'title': 'other title'}
        response = self.client.post(url, data)
        category = Category.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:category_list')
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(category.title, data['title'])


class AuthCategoryDeleteTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user
        permission = Permission.objects.get(codename='delete_category')
        cls.user.user_permissions.add(permission)
        cls.category = Category.objects.create(title='category')

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_delete_category_success(self):
        response = self.client.get(reverse('news_client:category_delete', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)

    def test_delete_category_success(self):
        response = self.client.post(reverse('news_client:category_delete', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news_client:category_list')
        self.assertEqual(response.url, redirect_url)
