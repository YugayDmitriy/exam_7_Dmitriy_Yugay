from django.shortcuts import render
from webapp.models import Visitors


def index(request):
    visitors_list = Visitors.objects.all()
    choices = Visitors.CHOISES
    context = {
        'visitors_list': visitors_list,
        'choices': choices
    }
    return render(request, 'index.html', context=context)
