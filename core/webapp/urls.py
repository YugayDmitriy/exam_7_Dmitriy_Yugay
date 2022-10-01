from django.urls import path

from .views.base import index

urlpatterns = [
    path('', index, name='index'),
]