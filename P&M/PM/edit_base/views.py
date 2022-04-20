from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import Authorization


class Auth(FormView):
    template_name = 'edit_base/auth.html'
    form_class = Authorization
    success_url = 'edit_base/edit'
class Edit(TemplateView):
    template_name = 'edit_base/edit'




# Create your views here.
