from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = "auth/login.html"


class Password_change(PasswordChangeView):
    template_name = "auth/password_change.html"
    success_url = reverse_lazy('authentication:password_change_done')


class Password_reset(PasswordResetView):
    template_name = "auth/password_reset_email.html"
    subject_template_name = "auth/password_reset_subject.txt"
    email_template_name = "auth/password_reset_email.txt"
    success_url = reverse_lazy('authentication:password_reset_done')
    from_email = 'grodnopythonclassdemo@gmail.com'


class Reset_confirm(PasswordResetConfirmView):
    template_name = "auth/password_reset_confirm.html"
    success_url = reverse_lazy('authentication:password_reset_complete')
