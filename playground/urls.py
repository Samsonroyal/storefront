from django.urls import path
from .views import *

# URL Configuration
urlpatterns = [
    path('hello/', say_hello), 
    path('queries/', QueryView.as_view(), name='query-view'),
]
