from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
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