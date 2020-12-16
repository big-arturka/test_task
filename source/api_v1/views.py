from rest_framework.response import Response
from rest_framework.views import APIView

from api_v1.serializers import ArticleSerializer, CategorySerializer
from news_client.models import Article, Category


class GetArticleListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleSerializer(objects, many=True)
        return Response(serializer.data)


class GetCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Category.objects.all()
        serializer = CategorySerializer(objects, many=True)
        return Response(serializer.data)
