from django.urls import path
from .views import Auth, Edit

app_name = "authentication"
urlpatterns = [
    path('', Auth.as_view(), name='auth'),
    path('edit/', Edit.as_view(), name='edit')
]


