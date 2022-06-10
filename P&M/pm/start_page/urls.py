from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = "start_page"
urlpatterns = [
    path('base/delete/<int:pk>', DeleteMedcine.as_view(), name='delete'),
    path('base/update/<str:general_url_name>', update_medcine, name='update_medcine'),
    path('base/update/', UpdateBase.as_view(), name='update'),
    path('base/create/', create_medcine, name='create'),
    path('base/', login_required(TemplateView.as_view(template_name='start_page/base_operations.html')), name='base'),
    path('about/', TemplateView.as_view(template_name="start_page/about.html"), name='about'),
    path('policy/', TemplateView.as_view(template_name="start_page/policy.html"), name='policy'),
    path('search/', search_medcine, name="search"),
    path('search/<str:url_name>', search_param, name="search_param"),
    path('error/', TemplateView.as_view(template_name="start_page/not_in_base.html"), name="error"),
    path('', index, name='home'),
    path('api/tags/', add_tags, name='tags')
]
