from django import forms
from django.forms import ModelForm
from .models import Medcine, Synonyms, General_sources

class Search(forms.Form):
    medcine_name = forms.CharField(max_length=30,
                                   widget=forms.TextInput(attrs={'class': 'form-control me-5',
                                                                 'placeholder': 'Введите название препарата',
                                                                 'id':'search'}), label="")

class Add_medcine(ModelForm):
    class Meta:
        model = Medcine
        fields = ['international_name', 'general_info']
        labels = ['МНН', 'Информация']
class Add_synonyms(ModelForm):
    class Meta:
        model = Synonyms
        fields = ['comm_name', 'url_name']
        labels = ['Торговое наименование', 'Краткое название']
class Add_literature(ModelForm):
    class Meta:
        model = General_sources
        fields = ['source_name']
        labels = ['Литература']
