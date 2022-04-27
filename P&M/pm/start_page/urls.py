from django.urls import path
from . import views
app_name = "start_page"
urlpatterns = [
    path('base/create/', views.create_medcine, name='create'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('search/', views.search_medcine, name="search"),
    path('search/<str:url_name>', views.search_param, name="search_param"),
    path('error/', views.error, name="error"),
    path('', views.index, name='home'),
    path('api/tags/', views.add_tags, name='tags')
]

