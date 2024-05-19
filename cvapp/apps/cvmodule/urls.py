from django.urls import path,include 
from apps.cvmodule import views

urlpatterns = [
    path('',views.index,name='index'),
     path('imag',views.imag),
     path('book/<int:bId>',views.book)
     ]
