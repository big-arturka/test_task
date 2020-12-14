from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from news_client.forms import ArticleForm
from news_client.models import Article


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'articles'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(LoginRequiredMixin, DetailView):
    template_name = 'article/article_view.html'
    model = Article
    context_object_name = 'article'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleForm
    model = Article

    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        return redirect('news_client:article_view', pk=article.pk)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    model = Article
    permission_required = 'webapp.change_article'

    def form_valid(self, form):
        article = form.save()
        return redirect('news_client:article_view', pk=article.pk)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    success_url = reverse_lazy('news_client:index')
