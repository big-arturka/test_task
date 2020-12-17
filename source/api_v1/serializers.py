from django.contrib.auth import get_user_model
from rest_framework import serializers
from news_client.models import Article, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'parent_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']


class ArticleSerializer(serializers.ModelSerializer):
    category_name = CategorySerializer(read_only=True, source='category_id')
    author_name = UserSerializer(read_only=True, source='user_id')

    class Meta:
        model = Article
        fields = ['id', 'title', 'description', 'category_id', 'category_name', 'user_id', 'author_name']