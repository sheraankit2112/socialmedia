from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from p.serializer import dataserializer
from my.models import mydata

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
    if request.method=="POST":
        data=request.body
        stream=io.BytesIO(data)
        python_data=JSONParser().parse(stream)
        id=python_data.get("id",None)
        if id is not None:
            ob=mydata.objects.get(id=id)
            