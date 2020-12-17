from django.contrib.auth import get_user_model
from django.db.models import Model
from django.test import TestCase
from news_client.forms import ArticleForm, CategoryForm
from news_client.models import Category


class ArticleFormTestCase(TestCase):
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

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_form_success(self):
        form = ArticleForm(data={'title': 'test title', 'description': 'test description', 'category_id': self.category})
        self.assertTrue(form.is_valid())

    def test_form_error_not_required_fields(self):
        form = ArticleForm(data={'title': 'test title', 'description': 'test description'})
        self.assertFalse(form.is_valid())


class CategoryFormTestCase(TestCase):
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

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_form_success(self):
        form = CategoryForm(data={'title': 'test title'})
        self.assertTrue(form.is_valid())

    def test_form_error_not_required_fields(self):
        form = CategoryForm(data={'parent_id': self.category})
        self.assertFalse(form.is_valid())