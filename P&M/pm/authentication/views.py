from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView


class Login(LoginView):
    template_name = "auth/login.html"
    success_url = reverse_lazy("authentication:login")


class PasswordChange(PasswordChangeView):
    template_name = "auth/password_change.html"
    success_url = reverse_lazy('authentication:password_change_done')


class PasswordReset(PasswordResetView):
    template_name = "auth/password_reset_email.html"
    subject_template_name = "auth/password_reset_subject.txt"
    email_template_name = "auth/password_reset_email.txt"
    success_url = reverse_lazy('authentication:password_reset_done')
    from_email = 'grodnopythonclassdemo@gmail.com'


class ResetConfirm(PasswordResetConfirmView):
    template_name = "auth/password_reset_confirm.html"
    success_url = reverse_lazy('authentication:password_reset_complete')


class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'auth/profile.html'
