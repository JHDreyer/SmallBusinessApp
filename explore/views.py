from django.shortcuts import render
from django.db.models import Q
from customer_profile.models import Business

def explore(request):
    options = Business.objects.all()
    return render(request, 'explore.html', {'options': options})

def search(request):

    query = request.GET.get('exploreSearch')
    options = Business.objects.filter(Q(name__icontains=query) | Q(type__icontains=query))

    if len(options) == 0:
        print(len(options))
        options = False

    return render(request, 'explore.html', {'options': options})

