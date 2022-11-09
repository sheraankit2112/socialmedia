from django.core.mail import send_mail

from django.shortcuts import redirect,render


def home(request):
    if request.method=="POST":
        message=request.POST.get('message')
        reciever=request.POST.get('reciever')

        send_mail("hello",str(message),"akshera2112@gmail.com",[reciever])
        return redirect("/")

    return render(request,"home.html")

