from django.shortcuts import render
from webapp.models import Visitors


def index(request):
    return render(request, 'index.html')
