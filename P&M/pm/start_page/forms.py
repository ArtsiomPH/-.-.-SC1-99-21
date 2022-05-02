from django import forms
from django.forms import ModelForm
from .models import Medcine, Synonyms, General_sources
from django.core.validators import RegexValidator


class Search(forms.Form):
    medcine_name = forms.CharField(max_length=40,
                                   widget=forms.TextInput(attrs={'class': 'form-control me-5',
                                                                 'placeholder': 'Введите название препарата',
                                                                 'id': 'search'}), label="")


class Add_medcine(ModelForm):
    international_name = forms.CharField(max_length=40, label="МНН", required=True, validators=[RegexValidator(
        regex='^[A-Z][a-z]+$'
    )],
                                         error_messages={'invalid': 'Введите название латиницей с большой буквы'},
                                         help_text="Ввод латиницей с большой буквы", widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    general_info = forms.CharField(min_length=10, label="Информация", required=True, validators=[RegexValidator(
        regex='^[А-Я][а-яА-Я]+$'
    )],
                                   error_messages={'invalid': 'Введите информацию кирилицей'},
                                   help_text="Ввод кириллицей с большой буквы", widget=forms.Textarea(attrs={'autocomplete': 'off'}))

    general_documentation = forms.URLField(required=True, label='Ссылка на документацию', widget=forms.URLInput(attrs={'placeholder': 'https://example.com', 'autocomplete': 'off'}))

    class Meta:
        model = Medcine
        fields = ['international_name', 'general_info', 'general_documentation']
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
