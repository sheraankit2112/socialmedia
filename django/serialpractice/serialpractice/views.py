from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from serialpractice.serializer import dataserializer
from rest_framework.renderers import JSONRenderer
from my.models import data
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    if request.method=="POST":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        d=dataserializer(data=python_data)
        if d.is_valid():
            d.save()
            msg={"msg":"data created"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        else:
            msg={"msg":"data invalid"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("data created")

def read(request):
    if request.method=="GET":
        dataa=request.body
        stream=io.BytesIO(dataa)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=data.objects.get(id=id)
            serial=dataserializer(ob)
            print(serial)
            
            
            json_data=JSONRenderer().render(serial.data)

            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("data fetched")

@csrf_exempt
def update(request):
    if request.method=="PUT":
        dataa=request.body
        stream=io.BytesIO(dataa)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=data.objects.get(id=id)
            serial=dataserializer(ob,data=python_data,partial=True)
            if serial.is_valid():
                serial.save()
                msg={"msg":"data updated"}
                json_data=JSONRenderer().render(msg)
                return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("data updated")



