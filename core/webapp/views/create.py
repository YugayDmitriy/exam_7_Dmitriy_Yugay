from django.shortcuts import render
from webapp.models import Visitors
from django.contrib import messages


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        discription = request.POST['discription']
        created_at = request.POST['created_at']
        item = Visitors(name=name, discription=discription, created_at=created_at)
        item.save()
        messages.info(request, "Задача успешно добавлена")
    else:
        pass
    item_list = Visitors.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'create.html', context=context)
