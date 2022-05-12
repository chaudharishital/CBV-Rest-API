from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.generic import View
from django.utils.decorators import method_decorator
import io
from django.views.decorators.csrf import csrf_exempt
from API.serializer import EmployeeSerializer
# Create your views here.csrf_exempt
@method_decorator(csrf_exempt , name='dispatch')
class createdata(View):
    def post(self,request):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(pythondata)
        return JsonResponse(serializer.errors,safe=False)
