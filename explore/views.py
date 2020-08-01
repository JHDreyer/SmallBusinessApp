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
<<<<<<< HEAD
        Q(businessname__icontains=query) | Q(type__icontains=query))
=======
        Q(bussinessname__icontains=query) | Q(type__icontains=query))
>>>>>>> 9c244eca1b14b6bae58f2fc0003a4c1ee4fa6e3c

    if len(options) == 0:
        print(len(options))
        options = False

    return render(request, 'explore.html', {'options': options})

def about(request):
    return render(request, 'about.html')

class BusinessDetailView(DetailView):
    model = Business
