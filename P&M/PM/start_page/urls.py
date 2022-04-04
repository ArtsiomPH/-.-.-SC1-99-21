from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from . import views
app_name = "start_page"
urlpatterns = [
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('search/', views.search_medcine, name="search"),
    path('search/<str:url_name>', views.search_param, name="search_param"),
    path('error/', views.error, name="error"),
    path('', views.index, name='home')
]

