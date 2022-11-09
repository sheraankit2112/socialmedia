from functools import partial
import json
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from my.models import userdata
from serial2.serializer import dataSerializer
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
            msg={"msg":"data inserted"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("data not createt")


def read(request):
    if request.method=="GET":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=userdata.objects.get(id=id)
            s=dataSerializer(ob)
            json_data=JSONRenderer().render(s.data)

            return HttpResponse(json_data,content_type="application/json")
        else:
            ob=userdata.objects.all()
            s=dataSerializer(ob,many=True)
            json_data=JSONRenderer().render(s.data)

            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse("hello")

@csrf_exempt
def update(request):
    if request.method=="PUT":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            d=userdata.objects.get(id=id)
            complex_data=dataSerializer(d,data=python_data,partial=True)
            if complex_data.is_valid():
                complex_data.save()
                msg={"msg":"data changed"}
                json_data=JSONRenderer().render(msg)

                return HttpResponse(json_data,content_type="application/json")
        else:
            msg={"msg":"data not changed"}
            return HttpResponse(json_data,content_type="application/json")

            

            

