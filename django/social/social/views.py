from cmath import log
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from social.forms import loginform,signupform
from django.core.mail import send_mail
from database.models import userdata,userposts,userbio
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.hashers import make_password
from django import forms

import uuid
from django.contrib import messages

def loginpage(request):
    fm=loginform()
    if request.method=="POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            global username
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/homepage")

    return render(request,"login.html",{"form":fm})

def signup(request):
    fm=signupform
    if request.method=="POST":
        fm=signupform(request.POST,request.FILES)
        if fm.is_valid():
            name=request.POST.get("name")
            usernamee=request.POST.get("username")
            email=request.POST.get("email")
            mobile=request.POST.get("mobile")
            password=request.POST.get("password")
            cpassword=request.POST.get("cpassword")
            profile=request.FILES.get("profile")
            newuser= User.objects.create_user(username=usernamee,email=email,password=password).save()
            userbio(name=name,username=usernamee,email=email,profile=profile,mobile=mobile).save()
            messages.success(request,"Account created successfully")
            return redirect("/")

            
    return render(request,"signup.html",{"form":fm})

def logoutbutton(request):
    logout(request)
    return redirect("/")


def homepage(request):
    posts=userposts.objects.all()
    return render(request,"homepage.html",{"posts":posts})

def password_enter_new(request,toke):
    ob=userdata.objects.get(token=toke)
    userr=ob.username

    if request.method=="POST":
        passwordd=request.POST.get("password")
        confirmpas=request.POST.get("cpas")
        if passwordd==confirmpas:
            for i in User.objects.filter(username=userr):
                id=i.id
                userrr=i.username
                email=i.email
            main_password=make_password(passwordd)
            User(id=id,password=main_password,username=userrr,email=email).save()
            messages.success(request,"password changed successfully")
            return redirect(f"/passwordnew/{toke}")
        else:
            messages.error(request,"password do not match")
            return redirect(f"/passwordnew/{toke}")

    return render(request,"password_newpas.html")



def forgot_password(request):
    
    if request.method=="POST":
        
        usernames=request.POST.get("username")
        if User.objects.filter(username=usernames).exists():
            users=User.objects.get(username=usernames)
            user_email=users.email
            
            
            token=str(uuid.uuid4())
            if userdata.objects.filter(username=usernames).exists():
                obb=userdata.objects.get(username=usernames)
                id=obb.id

                userdata(id=id,username=usernames,token=token).save()
                send_mail("Namaste media password reset","This is your link for reset the password" +" " + f"http://127.0.0.1:3456/passwordnew/{token}","akshera2112@gmail.com",[user_email])
                messages.success(request,"An email has sent")
                return redirect("/forgotpassword")
            else:
                userdata(username=usernames,token=token).save()
                send_mail("Namaste media password reset","This is your link for reset the password" +" " + f"http://127.0.0.1:3456/passwordnew/{token}","akshera2112@gmail.com",[user_email])
                messages.success(request,"An email has sent")
                return redirect("/forgotpassword")

        else:
            messages.error(request,"username not found")
            return redirect("/forgotpassword")

    return render(request,"check_username.html")


def uploadpost(request):
    if request.method=="POST":
        post=request.FILES.get("post")
        caption=request.POST.get("caption")
        userposts(username=username,post=post,caption=caption).save()
        messages.success(request,"uploaded successfully")
        return redirect("/homepage")

    return render(request,"uploadpost.html")
