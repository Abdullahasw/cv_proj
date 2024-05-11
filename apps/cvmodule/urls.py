from django.urls import path,include 
from apps.cvmodule import views

urlpatterns = [
    path('',views.index,name='index')
]
