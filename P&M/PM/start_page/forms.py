from django import forms

class Search(forms.Form):
    medcine_name = forms.CharField(max_length=30,
                                   widget=forms.TextInput(attrs={'class':'form-control',
                                                                 'placeholder':'Введите название препарата'}), label="")
