import secrets

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class UserCreateView(CreateView):
    """Контроллер для создания пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        "login": "Вход",
    }

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейти по ссылке для подтверждения почты {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

    @staticmethod
    def email_verification(request, token):
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))


class UserResetPasswordView(FormView):
    """Контроллер для сброса пароля пользователя"""
    model = User
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        random_password = secrets.token_hex(16)
        for user in form.get_users(email):
            user.set_password(random_password)
            user.save()
        send_mail(
            subject='Пароль сброшен',
            message=f'Ваш пароль {random_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('mailing:info-view')
    extra_context = {
        "profile": "Профиль",
        "save": "Сохранить",
    }

    def get_object(self, queryset=None):
        return self.request.user
