from django.urls import path
from django.urls import re_path
from django.views.generic import TemplateView
from . import views
app_name = "start_page"
urlpatterns = [
    re_path(r'^about', TemplateView.as_view(template_name='start_page/about.html')),
    re_path(r'^policy', TemplateView.as_view(template_name='start_page/policy.html')),
    re_path(r'^search', views.search_medcine, name="search"),
    re_path(r'^error', TemplateView.as_view(template_name='start_page/not_in_base.html')),
    path('', views.index, name='home')
]

