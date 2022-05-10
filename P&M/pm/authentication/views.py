from django.contrib.auth.views import LoginView, PasswordChangeView

class Login(LoginView):
    template_name = "auth/login.html"

class Password_change(PasswordChangeView):
    template_name = "auth/password_change.html"
    success_url = "login"
