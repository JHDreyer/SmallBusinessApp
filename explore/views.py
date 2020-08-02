from django.shortcuts import render
from django.db.models import Q
from businesses.models import Business, Product
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


def explore(request):
    options = Business.objects.all()
    return render(request, 'explore.html', {'options': options})


def search(request):

    query = request.GET.get('exploreSearch')
    options = Business.objects.filter(
        Q(businessname__icontains=query) | Q(businesstype__icontains=query))

    if len(options) == 0:
        print(len(options))
        options = False

    return render(request, 'explore.html', {'options': options})


def about(request):
    return render(request, 'about.html')


def BusinessDetailView(request, pk):
    business = get_object_or_404(Business, pk=pk)
    products = Product.objects.filter(business=business)
    context = {
        'business': business,
        'products': products
    }
    return render(request, 'businesses/business_detail.html', context=context)


def ProductDetailView(request, pk, slug):
    query = slug
    business = get_object_or_404(Business, pk=pk)

    products = Product.objects.filter(Q(name__icontains=query))

    context = {
        'business': business,
        'products': products
    }
    return render(request, 'businesses/product_detail.html', context=context)
