from django import forms

from news_client.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'category_id', 'user_id', 'image']
