from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import Authorization


class Auth(FormView):
    template_name = 'authentication/auth.html'
    form_class = Authorization
    success_url = 'authentication/edit'
class Edit(TemplateView):
    template_name = 'authentication/edit'




# Create your views here.
