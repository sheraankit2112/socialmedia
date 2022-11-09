from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from my.models import studentdata
from rest.serializer import dataserializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@api_view(['GET','POST','PUT'])
def crud(request):
    if request.method=="POST":
        serial=dataserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            msg={'msg':'data inserted'}
            return Response(msg)
        else:
            return Response({'msg','data not inserted'})

    if request.method=="GET":
        id=request.data.get("id",None)
        if id is not None:
            ob=studentdata.objects.get(id=id)
            serial=dataserializer(ob)
            return Response(serial.data)
        else:
            ob=studentdata.objects.all()
            serial=dataserializer(ob,many=True)

    if request.method=="PUT":
        new=request.data
        id=request.data.get("id",None)
        if id is not None:
            old=studentdata.objects.get(id=id)
            serial=dataserializer(old,data=new,partial=True)
            if serial.is_valid():
                serial.save()
                return Response({"msg":"data updated"})
        else:
            return Response({"msg":"wrong details"})


    