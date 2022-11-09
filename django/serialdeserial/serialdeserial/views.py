from django.shortcuts import render
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from my.models import studentdata
from serialdeserial.serializer import dataserializer
from rest_framework.renderers import JSONRenderer

def create(request):
    if request.method=="POST":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        complex_data=dataserializer(data=python_data)
        if complex_data.is_valid():
            complex_data.save()
            msg={"msg":"data created"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("data not created")


def read(request):
    if request.method=="GET":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=studentdata.objects.get(id=id)
            dataa=dataserializer(data=ob)
            json_data=JSONRenderer().render(dataa.data)
            return HttpResponse(json_data,content_type="application/json")

        else:
            ob=studentdata.objects.all()
            dataa=dataserializer(data=ob,many=True)
            json_data=JSONRenderer().render(dataa.data)
            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("ok")

def update(request):
    if request.method=="PUT":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=studentdata.objects.get(id=id)
            dataa=