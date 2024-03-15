# example/urls.py
from django.urls import path

from .views import *


urlpatterns = [
    path('', index),
    path('4th/', fourth, name='4th'),
    path('5th/', fifth, name='5th'),
    path('6th/', six, name='6th'),
    path('7th/', seven, name='7th'),
    path('8th/', eight, name='8th'),
]