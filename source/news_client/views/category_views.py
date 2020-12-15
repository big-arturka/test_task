from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from news_client.forms import CategoryForm
from news_client.models import Category


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'category/category_create.html'
    form_class = CategoryForm
    model = Category
    permission_required = 'news_client.add_category'

    def get_success_url(self):
        return reverse('news_client:category_list')


class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'category/category_update.html'
    form_class = CategoryForm
    model = Category
    permission_required = 'news_client.change_category'

    def get_success_url(self):
        return reverse('news_client:category_list')


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    model = Category
    permission_required = 'news_client.delete_category'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('news_client:category_list')