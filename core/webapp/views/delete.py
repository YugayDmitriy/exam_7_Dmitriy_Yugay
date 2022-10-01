from django.contrib import messages
from django.shortcuts import redirect, render
from webapp.models import Visitors


def delete(request, myid):
    item = Visitors.objects.get(id=myid)
    context = {
        'item': item,
    }
    return render(request, 'confirm_delete.html', context=context)


def confirm_delete(request, myid):
    item = Visitors.objects.get(id=myid)
    item.delete()
    messages.info(request, 'Задача успешно удалена')
    return redirect('index')
