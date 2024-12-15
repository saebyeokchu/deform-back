from django.urls import path
from . import views

urlpatterns = [
    path('getClosestColor/', views.getClosestColor, name='getClosestColor'),
    path('getColors/', views.getColors, name='getColors'),
]
