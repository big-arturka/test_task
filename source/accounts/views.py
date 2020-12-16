from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView


from accounts.forms import MyUserCreationForm, UserChangeForm, PasswordChangeForm
from accounts.models import CustomUser


class RegisterView(PermissionRequiredMixin, CreateView):
    model = get_user_model()
    template_name = 'users/user_create.html'
    form_class = MyUserCreationForm
    permission_required = 'news_client.add_user'

    def get_success_url(self):
        return reverse('accounts:list')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0


class UsersListView(LoginRequiredMixin, ListView):
    template_name = 'users/users_view.html'
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 4

    def get_queryset(self):
        return CustomUser.objects.all()


class UserChangeView(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'users/user_change.html'
    context_object_name = 'user_obj'
    permission_required = 'news_client.change_user'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'
    permission_required = 'news_client.change_user'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'users/user_delete.html'
    model = get_user_model()
    context_object_name = 'user'
    success_url = reverse_lazy('accounts:list')
    permission_required = 'news_client.delete_user'

    def has_permission(self):
        user = self.get_object()
        return super().has_permission() or user == self.request.user
