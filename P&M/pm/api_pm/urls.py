from django.urls import path, include, re_path
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r"medcine", MedcineViewSet)
router.register(r"synonyms", SynonymsViewSet)

urlpatterns = [
    path('v1/drf-auth/', include('rest_framework.urls')),
    # path('v1/medcinelist/', MedcineApiList.as_view()),
    # path('v1/medcinelist/<int:pk>/', MedcineApiDetail.as_view()),
    # path('v1/synonymslist/', SynonymsApiList.as_view()),
    # path('v1/synonymslist/<int:pk>', SynonymsApiDetail.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))

]
