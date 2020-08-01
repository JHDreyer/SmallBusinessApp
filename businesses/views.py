from django.shortcuts import render
from .models import Business, Product, Service
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, UpdateView, DeleteView, ListView)
from django.urls import reverse_lazy
from .forms import BusinessForm, ServiceForm, ProductForm


def index(request):
    return render(request, 'business/profile.html')


def manageBusiness(request):

    if request.method == 'POST':
        if request.POST.get('businessSelect'):
            selected_business = request.POST.get('businessSelect')
            options = Business.objects.filter(
                Q(bussinessname__icontains=selected_business))

            products = Product.objects.all()

            if len(products) == 0:
                products = False

            return render(request, 'customer/business_manage.html', {'options': options, 'products': products})
    else:
        user_name = request.user
        options = Business.objects.filter(Q(user=user_name))

    return render(request, 'customer/manage.html', {'options': options})


class BusinessUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'businesses/business_update.html'

    login_url = '/login/'

    redirect_field_name = 'businesses/business_detail.html'

    form_class = BusinessForm

    model = Business


class BusinessDeleteView(DeleteView, LoginRequiredMixin):
    model = Business
    success_url = reverse_lazy('businesses:list')


class BusinessCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'

    redirect_field_name = 'businesses/business_detail.html'

    form_class = BusinessForm

    model = Business

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BusinessListView(ListView):
    model = Business

    def get_queryset(self):
        return Business.objects.filter(user=self.request.user)


class ProductCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'

    redirect_field_name = 'businesses/product_detail.html'

    form_class = ProductForm

    model = Product

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.business.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ServiceCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'

    redirect_field_name = 'businesses/service_detail.html'

    form_class = ServiceForm

    model = Service

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.business.user = self.request.user
        self.object.save()
        return super().form_valid(form)


'''def BusinessAdmin(request):
    # this is effectively replaced by manage business
    user_name = request.user
    options = Business.objects.filter(Q(user=user_name), Q(name__icontains=id))
    
    return render(request, 'customer/business_manage.html', {'options': business})
'''
