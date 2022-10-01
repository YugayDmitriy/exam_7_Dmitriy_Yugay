from django.shortcuts import render
from webapp.models import Visitors


def edit(request, myid):
    sel_visit = Visitors.objects.get(id=myid)
    visit_list = Visitors.objects.all()
    context = {
        'sel_visit': sel_visit,
        'visit_list': visit_list,
    }
    return render(request, 'index.html', context=context)
