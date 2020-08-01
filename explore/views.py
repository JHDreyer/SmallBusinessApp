from django.shortcuts import render
from django.db.models import Q
from businesses.models import Business
from django.views.generic import DetailView


def explore(request):
    options = Business.objects.all()
    return render(request, 'explore.html', {'options': options})


def search(request):

    query = request.GET.get('exploreSearch')
    options = Business.objects.filter(
        Q(bussinessname__icontains=query) | Q(type__icontains=query))

    if len(options) == 0:
        print(len(options))
        options = False

    return render(request, 'explore.html', {'options': options})


class BusinessDetailView(DetailView):
    model = Business
