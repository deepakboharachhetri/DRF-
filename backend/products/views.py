from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import generics
import json 
import requests 
from django.forms.models import model_to_dict
def home(request,*args,**kwargs):
    getting_params=request.body
    print(type(getting_params))
    params_str=json.loads(getting_params.decode('utf-8'))
 

    getting_data=request.GET
    print(type(getting_data))
    # print(request.headers,request.content_type,request)
    data={}
    
    data['params']=params_str
    data['data']=getting_data
    print(data)
    # data={
    #     "id":1,
    #     "name":"Deepak",
    #     "last name":"Bohara Chhetri"
    # }
    return JsonResponse(data)  

from .models import Product
from .serializers import *
class productCreateApiView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        price=serializer.validated_data.get('price')
        if content is None :
            content=title
        serializer.save(content=content)
        
        return super().perform_create(serializer)


class productRetrieveApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class productListApiView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class productListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def perform_create(self, serializer):
        print("new product created ")
        return super().perform_create(serializer)
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
@api_view(['GET','POST'])
def create_all_generics_view(request,pk=None,*args,**kwargs):
    if request.method== "GET":
        if pk is not None :
            obj=get_object_or_404(Product,pk=pk)
            serializer=ProductSerializer(obj,many=False).data
            return Response(serializer,200)
        query=Product.objects.all()
        serializer=ProductSerializer(query,many=True).data
        return Response(serializer)
    if request.method=="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
          serializer=serializer.save()
          return Response(serializer.data,status=2000)
        return Response({"error":"bad request"},status=404)

        