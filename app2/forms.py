from dataclasses import fields
from pyexpat import model
from django import forms
from app2.models import User


class UserCreationForm(forms.ModelForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists() is True:
            raise forms.ValidationError('email id already Taken')

    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.ModelForm):
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if User.objects.filter(email=email, password=password).exists() is False:
            raise forms.ValidationError('email or password is incorrect')
        else:
            self.user = User.objects.get(email=email, password=password).id

    class Meta:
        model = User
        fields = '__all__'
