from .models import User
from django.forms import ModelForm

class Authorization(ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password']
        labels = ['логин', 'пароль']


