from django.contrib.auth import get_user_model
from django.db.models import Model
from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response
from news_client.models import Article, Category


EXAMPLE_DATA = [{
                    "id": 1,
                    "title": "test",
                    "description": "test",
                    "category_id": 1,
                    "category_name": {
                        "title": "category",
                        "parent_id": None
                    },
                    "user_id": 1,
                    "author_name": {
                        "username": "admin"
                    }
                }]


class ApiGetArticleTestCase(TestCase):
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
        cls.article = Article.objects.create(title='test', category_id=cls.category, description='test',
                                             user_id=cls.user)

    def test_get_article_list(self):
        response = self.client.get(reverse('api_v1:get_article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), Response)
        self.assertJSONEqual(response.content.decode(), EXAMPLE_DATA)
