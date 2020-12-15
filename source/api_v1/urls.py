from django.urls import path
from api_v1.views import GetArticleListView, GetCategoryListView

app_name = 'api_v1'


urlpatterns = [
    path('articles/', GetArticleListView.as_view(), name='get_article_list'),
    path('categories/', GetCategoryListView.as_view(), name='get_category_list'),
]