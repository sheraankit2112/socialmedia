from audioop import reverse
from cmath import log
from django.shortcuts import redirect,render
from my.forms import loginform,signupform
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from my.models import userdata,userpost
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page
@cache_page(30)
def loginn(request):
    global username
    if request.session:
        if "username" in request.session:
            username=request.session['username']
            password=request.session['password']
            fm=loginform({"username":username,"password":password})
        else:
            fm=loginform()
    else:
        fm=loginform()
    
    if request.method=="POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            
            username=request.POST.get('username')
            print(username)
            password=request.POST.get('password')
            p=str(password)
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                if request.session:
                    if "username" in request.session:
                        if username==request.session["username"]:
                            pass
                        else:
                            request.session["username"]=username
                            request.session['password']=p
                    else:
                        request.session["username"]=username
                        request.session['password']=p

                else:
                    request.session["username"]=username
                    request.session['password']=p


                messages.success(request,"successfully login")
                return redirect("/userpage")
                
                
                
            else:
                return HttpResponse("not")

    
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
            profile=request.FILES.get('profile')
            g=request.POST.get('group')
            newuser=User.objects.create_user(username,email,password)
            newuser.save()
            group=Group.objects.get(name=g)
            newuser.groups.add(group)
            userdata(username=username,name=name,profile=profile).save()
            messages.success(request,"successfully created account")
            return redirect("/")

    return render(request,"signup.html",{"form":fm})

def userpage(request):
    userd=userdata.objects.filter(username=username)
    print(userd)
    userp=userpost.objects.filter(username=username)
    if request.method=="POST":
        post=request.FILES.get('post')
        userpost(username=username,post=post).save()
        return redirect("/userpage")
    return render(request,"user.html",{"user":userd,"post":userp})

def deletepost(request,id):
    userpost(id=id).delete()
    return redirect("/userpage")

def allimages(request):
    userp=userpost.objects.all()
    return render(request,"all.html",{"data":userp})


    
