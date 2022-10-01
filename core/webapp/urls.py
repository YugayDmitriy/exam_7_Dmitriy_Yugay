from django.urls import path

from .views.base import index
from .views.create import create

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
]