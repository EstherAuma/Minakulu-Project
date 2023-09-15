from django.forms import ModelForm
from .models import *
from django import forms

class LoginForm(forms.ModelForm):
    class Meta:
        model = User

        fields =['username','password']



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'