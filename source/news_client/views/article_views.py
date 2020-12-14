from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from news_client.forms import ArticleForm
from news_client.models import Article


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(DetailView):
    template_name = 'article/article_view.html'
    model = Article
    context_object_name = 'article'


class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    model = Article


class ArticleUpdateView(UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    model = Article
    permission_required = 'webapp.change_article'


class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    success_url = reverse_lazy('webapp:index')
