from django import forms
from django.forms import ModelForm
from .models import Medcine, Synonyms, General_sources
from django.core.validators import RegexValidator


class Search(forms.Form):
    medcine_name = forms.CharField(max_length=40, min_length=3,
                                   widget=forms.TextInput(attrs={'class': 'form-control me-5',
                                                                 'placeholder': 'Введите название препарата', "id": "search"}), label="")


class Add_medcine(ModelForm):
    international_name = forms.CharField(max_length=300, label="МНН", required=True, validators=[RegexValidator(
        regex='^[A-Z][a-z0-9 ,-]+$'
    )],
                                         error_messages={'invalid': 'Введите название латиницей с большой буквы', 'null': 'Поле обязательно для заполнения'},
                                         help_text="Ввод латиницей с большой буквы", widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    general_info = forms.CharField(min_length=10, label="Информация", required=True, validators=[RegexValidator(
        regex='[а-яёА-Я0-9 .,!-]+$'
    )],
                                   error_messages={'invalid': 'Введите информацию кирилицей', 'null': 'Поле обязательно для заполнения'},
                                   help_text="Ввод кириллицей с большой буквы", widget=forms.Textarea(attrs={'autocomplete': 'off'}))

    general_documentation = forms.URLField(required=True, label='Ссылка на документацию', widget=forms.URLInput(attrs={'placeholder': 'https://example.com', 'autocomplete': 'off'}), error_messages={'invalid': 'Введите ссылку в нужном формате'})
    formula = forms.ImageField(label='Химическая формула')

    class Meta:
        model = Medcine
        fields = ['international_name', 'general_info', 'general_documentation']
        labels = ['МНН', 'Информация']


class Add_synonyms(ModelForm):
    comm_name = forms.CharField(max_length=50, label="Торговое наименование", validators=[RegexValidator(regex='^[А-Я][а-яёА-я0-9 -]+$')], error_messages={'invalid': 'Введите название кирилицей с большой буквы'}, help_text="Ввод кирилицей с большой буквы", widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    url_name = forms.CharField(max_length=50, label="Наименование на английском", validators=[RegexValidator(regex='^[a-z][a-zA-z -]+$')], error_messages={'invalid': 'Введите наименование латиницей с маленькой буквы'}, help_text="Ввод латиницей с маленькой буквы", widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    class Meta:
        model = Synonyms
        exclude = ['pub_date', 'medcine', 'id']


class Add_literature(ModelForm):
    source_name = forms.CharField(min_length=10, label="Источник", required=True, widget=forms.TextInput(attrs={'autocomplete': 'off'}), error_messages={'blank': 'Поле обязательно для заполнения', 'min_length': 'Минимум 10 символов'})
    class Meta:
        model = General_sources
        fields = ['source_name']

