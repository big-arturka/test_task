from django.urls import reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from news_client.forms import CategoryForm
from news_client.models import Category


class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'categories'
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Category.objects.all()


class CategoryCreateView(CreateView):
    template_name = 'category/category_create.html'
    form_class = CategoryForm
    model = Category


class CategoryUpdateView(UpdateView):
    template_name = 'category/category_update.html'
    form_class = CategoryForm
    model = Category


class CategoryDeleteView(DeleteView):
    model = Category

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('news_client:index')