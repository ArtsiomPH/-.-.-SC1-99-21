from django import forms

class Search(forms.Form):
    medcine_name = forms.CharField(max_length=30,
                                   widget=forms.TextInput(attrs={'class': 'form-control me-5',
                                                                 'placeholder': 'Введите название препарата',
                                                                 'id':'search'}), label="")
