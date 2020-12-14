from django import forms

from news_client.models import Article, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'category_id', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent_id']