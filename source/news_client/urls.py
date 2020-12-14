from django.urls import path

from news_client.views import IndexView

app_name = 'news_client'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
