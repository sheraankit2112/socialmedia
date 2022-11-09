from logging import PlaceHolder
from django import forms
from django.contrib.auth.models import User
from django.core import validators

choice=[
    ("ankit","ankit"),
    ("sahil","sahil")
]

def username_already(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError("username already exists")

def email_already(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError("Email already exists")



class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Name"}))
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}),validators=[username_already])
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"email"}),validators=[email_already])
    group=forms.ChoiceField(choices=choice)
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password"}))
    cpassword=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"confirm password"}))


    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            user=self.cleaned_data['cpassword']
            pas=self.cleaned_data['password']

            if user!=pas:
                raise forms.ValidationError("password not match")





class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password"}))

    def clean(self):
        cleaned_data=super().clean()
        if self.is_valid():
            user=self.cleaned_data['username']
            pas=self.cleaned_data['password']

            if User.objects.filter(username=user).exists():
                pass

            else:
                raise forms.ValidationError("username or password incorrect")
                

                

