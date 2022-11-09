from django import forms
from django.core import validators
from result_data.models import signup
def already_exist(value):
    if signup.objects.filter(email=value).exists():
        raise forms.ValidationError("(*Email already exists)")
def username_already(value):
    if signup.objects.filter(username=value).exists():
        raise forms.ValidationError("(*Username already exists)")


class signupform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control s2","placeholder":"Your name"}),validators=[validators.MaxLengthValidator(20,message="(*Length should be less than 20 letters)"),validators.MinLengthValidator(8,message="(*Length should be greater than 8 letters)")],label="name")
    email=forms.EmailField(validators=[validators.EmailValidator,already_exist],widget=forms.EmailInput(attrs={'class':"form-control s2","placeholder":"Your Email ID"}))
    username=forms.CharField(validators=[username_already],widget=forms.TextInput(attrs={'class':"form-control s2","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control s2","placeholder":"password"}))
    def clean_password(self):
        if self.is_valid():
            passw=self.cleaned_data['password']
            value = str(passw)
            count=0
            for i in value:
                if i.isdigit():
                    count=count+1

            if ("@" not in str(passw)) or (count==0):
                raise forms.ValidationError("*Password must include @ and numbers")
            else:
                return passw




class loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control s2","placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control s2","placeholder":"password"}))
    def clean_password(self):
        cleaned_data=super().clean()
        if self.is_valid():
            us=self.cleaned_data['username']
            p=self.cleaned_data['password']
            count=0
            if signup.objects.filter(username=us).exists():
                i=signup.objects.get(username=us)
                if i.password==p:
                    count=count+1
            if count==0:
                raise forms.ValidationError("(*username or password incorrect)")
