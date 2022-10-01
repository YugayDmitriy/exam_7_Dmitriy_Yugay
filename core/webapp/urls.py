from django.urls import path
from .views.delete import delete, confirm_delete
from .views.update import update
from .views.edit import edit
from .views.base import index
from .views.create import create

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('edit/<int:myid>/', edit, name='edit'),
    path('update/<int:myid>/', update, name='update'),
    path('delete/<int:myid>/', delete, name='delete'),
    path('confirm_delete/<int:myid>/', confirm_delete, name='confirm_delete')
]