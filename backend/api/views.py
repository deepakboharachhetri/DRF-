from django.forms.models import model_to_dict 
from products.models import Product 
from rest_framework.response import Response
from rest_framework.decorators import api_view
# @api_view(["GET"])
# def api_home(request,*arags,**kwargs):
#     """DRF API View"""
#     model_data=Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data =model_to_dict(model_data,fields=['id','title','price','sale_price'])
#     return Response(data,status=200)

from products.serializers import ProductSerializer

# @api_view(["GET"])
# def api_home(request,*arags,**kwargs):
#     """DRF API View"""
#     instance=Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         # data =model_to_dict(instance,fields=['id','title','price','sale_price'])
#         data=ProductSerializer(instance).data
#     return Response(data,status=200)



@api_view(["POST"])
def api_home(request,*arags,**kwargs):
    """DRF API View"""
    data=request.data
    serializer=ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        productserializer=serializer.save()
        data=serializer.data
        print(productserializer)
        return Response(productserializer.data,status=200)
    return Response({"invalid":"required data not given"},status=404)
