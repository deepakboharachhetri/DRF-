from django.urls import path 
from . import views 
urlpatterns=[
    path('',views.api_home ),
    path('product/',views.product_home ),
    path('product_dict/',views.product_home_using_modelstodict ),
    
]