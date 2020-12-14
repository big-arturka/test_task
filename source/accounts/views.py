from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from accounts.forms import MyUserCreationForm, UserChangeForm, PasswordChangeForm


class RegisterView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('index')
        return next_url


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0


class UsersListView(PermissionRequiredMixin, ListView):
    template_name = 'users/users_view.html'
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 4
    permission_required = 'accounts.can_view_users'

    def get_queryset(self):
        return User.objects.all()


class UserChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'users/user_change.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    template_name = 'users/user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.request.user == self.get_object()

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})