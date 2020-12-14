from django.urls import path
from django.urls import path, include

from news_client.views import IndexView, ArticleView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'news_client'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('article/', include([
            path('<int:pk>/', include([
                path('', ArticleView.as_view(), name='article_view'),
                path('update/', ArticleUpdateView.as_view(), name='article_update'),
                path('delete/', ArticleDeleteView.as_view(), name='article_delete'),
            ])),

            path('add/', ArticleCreateView.as_view(), name='article_create'),
        ])),
]
