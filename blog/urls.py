import imp
from importlib.resources import path
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]