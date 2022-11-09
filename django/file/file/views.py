from django.shortcuts import redirect,render
from my.models import filename

def uploadfile(request):
    ob=filename.objects.all()
    if request.method=="POST":
        
        file=request.FILES.get('file')

        filename(name=file).save()
        return redirect("/")
    return render(request,"hello.html",{"data":ob})




