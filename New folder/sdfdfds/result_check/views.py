from pickle import NONE
import re
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from result_data.models import studentBio
from result_data.models import studentData
from result_data.models import topperData,signup
from result_check.forms import signupform,loginform
from django.contrib.auth.models import User

from datetime import datetime
import csv
import pandas as pd
a=topperData.objects.all()
s=[]
count=0
global store
store=None
for i in a:
    count=count+1
    if i.sum>=250:
        s.append(i.sum)
overall_result=0


c=len(s)/count
final=round(c*100,2)

def about(request):
    return render(request,"about.html")

def home_page(request):
    name=None
    l=[]
    
    t=topperData.objects.all()
    for i in t:
        if i.sum>=400:
            l.append(i)
    l2=[]
    for j in l:
        for k in studentBio.objects.all():
            if j.uid==k.uid:
                l2.append(k)
    if request.method == "GET":
        name=request.GET.get('user')
        print(name)
    datas={"deta":l2,"final":final,"store":name}
    
        
    
    return render(request,"result_home.html",datas)

def result(request):
    d=None
    data=None
    namee=None
    uidd=None
    python=None
    soft=None
    java=None
    aptitude=None
    c_aptitude=None
    summ=None
    cal=None
    f_p=None
    result=None
    t=None
    l=None
    l2=None
    try:
        
        uidd=int(request.POST.get('roll'))
        namee=request.POST.get('name')
        
        data=studentBio.objects.get(uid=uidd)
        
        
        python=studentData.objects.get(uid=uidd,subject='python')
        soft=studentData.objects.get(uid=uidd,subject='soft skills')
        java=studentData.objects.get(uid=uidd,subject='java')
        aptitude=studentData.objects.get(uid=uidd,subject='Aptitude')
        c_aptitude=studentData.objects.get(uid=uidd,subject='Computing aptitude')
        summ=int(python.total)+int(soft.total)+int(java.total)+int(aptitude.total)+int(c_aptitude.total)
        cal=summ/500
        f_p=cal*100
        if f_p<50:
            result='fail'
        
        else:
            result='pass'
        
        l=[]
    
        t=topperData.objects.all()
        for i in t:
            if i.sum>=400:
                l.append(i)
        l2=[]
        for j in l:
            for k in studentBio.objects.all():
                if j.uid==k.uid:
                    l2.append(k)
        
            
    except:
        pass
    
    d={"roll":uidd,"summ":summ,"name":namee,"data":data,"datas":l2,"final":final,"python":python,"result":result,"java":java,"soft":soft,"aptitude":aptitude,"c_aptitude":c_aptitude}
    return render(request,"result_form.html",d)

def export(request):
    # nme = ["aparna", "pankaj", "sudhir", "Geeku"]
    # deg = ["MBA", "BCA", "M.Tech", "MBA"]
    # scr = [90, 40, 80, 98]
   
    # # dictionary of lists 
    # dict = {'name': nme, 'degree': deg, 'score': scr} 
     
    # df = pd.DataFrame(dict)
  
    # # saving the dataframe
    # response=df.to_csv(r'D:\file.csv', index=False)
    # return HttpResponse(response)
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment: filename:reviews'+  str(datetime.now()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['uid','Name','father name','mother name','department','Total marks'])
    
    bio =studentBio.objects.all()
    sum= topperData.objects.all()

    for i in bio:
        sum=topperData.objects.get(uid=i.uid)
        writer.writerow([i.uid, i.name,i.father_name,i.mother_name,i.department_name,sum.sum])

    return response
    # list of name, degree, score



def signupp(request):
    fm=signupform()
    if request.method == "POST":
        fm=signupform(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            email=fm.cleaned_data['email']
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            d=signup(names=name,email=email,username=username,password=password)
            d.save()
            return redirect("/thankyou")

    return render(request,"signup.html",{"form":fm,"final":final})

def login(request):
    global store
    store=None
    fm=loginform()
    if request.method == "POST":
        fm=loginform(request.POST)
        if fm.is_valid():
            name=signup.objects.filter(username=fm.cleaned_data['username'])
            for i in name:
                store=i.names
            url="/?user={}".format(store)
            return HttpResponseRedirect(url)
            
    

    return render(request,"login.html",{"form":fm,"final":final})

def thank(request):
    return render(request,"thankyou.html")