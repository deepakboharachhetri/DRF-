from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse,HttpResponse
def api_home(request,*args,**kwargs):
    body=request.body# byte string of json data 
    # print(body)
    try:
        data=json.loads(body)
    except Exception:
        pass
    print(data.keys())
    data['headers']=dict(request.headers) #request metadata 
    print(request.headers)
    data['content_type']=request.content_type

    data['params']=dict(request.GET)
    print(request.content_type)
    # print(request.GET)
    # print(request.POST)

    return JsonResponse(data)

from products.models import Product

def product_home(request,*args,**kwargs ):
    model_data=Product.objects.all().order_by("?").first()
    data ={}
    if model_data:
        data['title']=model_data.title
        data['content']=model_data.content
        data['price']=model_data.price
    return JsonResponse(data)

# serialization  above for each data 

# model instance  (model_data )
# turn a python dict
# return json to my client 

# using django forms
from django.forms.models import model_to_dict
# def product_home_using_modelstodict(request,*arags,**kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data =model_to_dict(model_data,fields=['id','title','price'])
#         print(data)
#         json_data_str=json.dumps(data)
#     # return JsonResponse(data)
#     return HttpResponse(json_data_str,headers={"content-type":"application/jsson"})


#from rest framework
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(["GET"])
def product_home_using_modelstodict(request,*arags,**kwargs):
    """DRF API View"""
    model_data=Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data =model_to_dict(model_data,fields=['id','title','price'])
    return Response(data,status=200)
