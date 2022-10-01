from django.shortcuts import render
from webapp.models import Visitors


def index(request):
    visit_list = Visitors.objects.exclude(status='blocked')
    context = {
        'visit_list': visit_list
    }
    return render(request, 'index.html', context=context)
