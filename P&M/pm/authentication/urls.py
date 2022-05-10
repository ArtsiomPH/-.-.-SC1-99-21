from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import Login, Password_change
from django.urls import path
app_name = "authentication"
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', Password_change.as_view(), name='password_change')

]


