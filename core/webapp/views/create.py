from django.shortcuts import render
from webapp.models import Visitors
from django.contrib import messages


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        item = Visitors(name=name, email=email, text=text)
        item.save()
        messages.info(request, "Задача успешно добавлена")
    else:
        pass
    visit_list = Visitors.objects.all()
    context = {
        'visit_list': visit_list
    }
    return render(request, 'index.html', context=context)
