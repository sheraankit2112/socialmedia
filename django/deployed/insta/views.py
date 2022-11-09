from django.http import HttpResponse
from django.shortcuts import redirect,render

from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from my.models import userbio,userpost
from my.forms import loginform,signupform
from django.contrib import messages
from django.views.decorators.cache import cache_page

@cache_page(100)
def loginn(request):
    if request.session:
        if "username" in request.session.keys():
            usernam=request.session["username"]
            password=request.session['password']
            fm=loginform({"username":usernam,"password":password})
        else:
            fm=loginform()
    else:
        fm=loginform()
    if request.method=="POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            global username
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if request.session:
                    if "username" in request.session.keys():
                        if username==request.session['username']:
                            pass
                        else:
                            request.session['username']=username
                            request.session['password']=password

                    else:
                        request.session['username']=username
                        request.session['password']=password

                else:
                    request.session['username']=username
                    request.session['password']=password
                messages.success(request,"Login successfully")
                return redirect("/homepage")

    return render(request,"login.html",{"form":fm})

def signup(request):
    fm=signupform()
    if request.method=="POST":
        fm=signupform(request.POST,request.FILES)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            username=fm.cleaned_data['username']
            email=fm.cleaned_data['email']
            password=fm.cleaned_data['password']
            profile=request.FILES.get("profile")
            group=fm.cleaned_data['group']

            new_user = User.objects.create_user(username,email,password)
            userbio(name=name,username=username,profile=profile).save()
            
            group=Group.objects.get(name=group)
            new_user.groups.add(group)
            
            messages.success(request,"Account created successfully")
            return redirect("/")
    
    return render(request,"signup.html",{"form":fm})

def homepage(request):
    ob=userbio.objects.get(username=username)
    poste=userpost.objects.filter(username=username)
    if request.method=="POST":
        pos=request.FILES.get("profile")
        userpost(username=username,post=pos).save()
        return redirect("/homepage")
    

    return render(request,"homepage.html",{"bio":ob,"post":poste})


def deletepost(request,id):
    userpost(id=id).delete()

    return redirect("/homepage")


def allusername(request):
    ob=userbio.objects.all()
    if request.method=="POST":
        n=request.POST.get("n")
        ob=userbio.objects.get(username__icontains=n)
        return redirect("/alluser")
    return render(request,"alluser.html",{"username":ob})



