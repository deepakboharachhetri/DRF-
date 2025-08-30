from django.urls import path
from . import views
from products.views import *
urlpatterns=[
    path('',views.home),
    path('create/',productCreateApiView.as_view()),
    path('<int:pk>/',productRetrieveApiView.as_view()),
    path('list/',productListApiView.as_view()),
    path('create_list/',productListCreateApiView.as_view()),


]