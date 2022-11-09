from functools import partial
from django.http import HttpResponse
import io
from my.models import data
from rest_framework.parsers import JSONParser
from serial.serializer import dataSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    if request.method=="POST":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)

        complex_data=dataSerializer(data=python_data)

        if complex_data.is_valid():
            complex_data.save()

            msg={"msg":"data created"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        
        else:
            msg={"msg":"data not created"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")



def read(request):
    if request.method=="GET":
        dataa=request.body
        stream=io.BytesIO(dataa)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=data.objects.get(id=id)
            s=dataSerializer(ob)
            json_data=JSONRenderer().render(s.data)

            return HttpResponse(json_data,content_type="application/json")

        else:
            ob=data.objects.all()
            s=dataSerializer(ob,many=True)
            json_data=JSONRenderer().render(s.data)

            return HttpResponse(json_data,content_type="application/json")
    return HttpResponse("data invalid")


@csrf_exempt
def update(request):
    if request.method=="PUT":
        dataa=request.body
        stream=io.BytesIO(dataa)
        python_data=JSONParser().parse(stream)
        ob=python_data.get("id")
        obb=data.objects.get(id=ob)
        complex_data=dataSerializer(obb,data=python_data,partial=True)

        if complex_data.is_valid():
            complex_data.save()
            msg={"msg":"data updated"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

        else:
            msg={"msg":"data updated"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def delete(request):
    if request.method=="DELETE":
        dataa=request.body
        stream=io.BytesIO(dataa)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id")
        
        if id is not None:
            data(id=id).delete()
            msg={"msg":"data deleted"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
            



