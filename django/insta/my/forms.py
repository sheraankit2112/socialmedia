from django import forms
from django.contrib.auth.models import User
from django.core import validators
choices=[
    ("doctor","doctor"),
    ("patient","patient")
]

def username_validator(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("Username already exists")

def email_validator(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email has already taken")


class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            user=self.cleaned_data['username']
            pas=self.cleaned_data['password']

            if not User.objects.filter(username=user).exists():
               

                
                raise forms.ValidationError("Username or password incorrect")


class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"name"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}),validators=[username_validator])
    email=forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"email"}),validators=[email_validator])
    group=forms.ChoiceField(choices=choices)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            pas=self.cleaned_data['password']
            cpas=self.cleaned_data['cpassword']
            if pas!=cpas:
                raise forms.ValidationError("Password do not match")
                