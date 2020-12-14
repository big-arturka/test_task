from django.views.generic import ListView
from news_client.models import Article


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Article.objects.all()

