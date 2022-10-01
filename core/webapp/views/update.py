from django.contrib import messages
from django.shortcuts import redirect
from webapp.models import Visitors


def update(request, myid):
    visit = Visitors.objects.get(id=myid)
    visit.name = request.POST['name']
    visit.email = request.POST['email']
    visit.text = request.POST['text']
    visit.save()
    messages.info(request, "Задача успешно отредактирована")
    return redirect('index')
