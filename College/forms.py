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


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'column1'})
        self.fields['last_name'].widget.attrs.update({'class': 'column1'})
        self.fields['gender'].widget.attrs.update({'class': 'column1'})
        self.fields['occupation'].widget.attrs.update({'class': 'column1'})
        self.fields['phone_number'].widget.attrs.update({'class': 'column1'})
        self.fields['nationality'].widget.attrs.update({'class': 'column2'})
        self.fields['district'].widget.attrs.update({'class': 'column2'})
        self.fields['tribe'].widget.attrs.update({'class': 'column2'})
        self.fields['email'].widget.attrs.update({'class': 'column2'})