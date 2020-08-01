from django.shortcuts import render, get_object_or_404, redirect
from businesses.models import Business, Product, Service
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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


@login_required
def add_product_to_business(request, pk):

    business = get_object_or_404(Business, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.business = business
            product.save()
            return redirect('/business')
            # return redirect('explore:product_detail', pk=business.pk)
    else:
        form = ProductForm()
    return render(request, 'businesses/product_form.html', {'form': form})


@login_required
def add_service_to_business(request, pk):

    business = get_object_or_404(Business, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            Service = form.save(commit=False)
            Service.business = Business
            Service.save()
            return redirect('explore')
            # return redirect('explore:service_detail', pk=Business.pk)
    else:
        form = ServiceForm()
    return render(request, 'businesses/service_form.html', {'form': form})


class ServiceListView(ListView):
    model = Service

    def get_queryset(self):
        return Service.objects.filter(user=self.request.user)


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'businesses/product_update.html'

    login_url = '/login/'

    redirect_field_name = 'businesses/product_detail.html'

    form_class = BusinessForm

    model = Business


class ServiceUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'businesses/service_update.html'

    login_url = '/login/'

    redirect_field_name = 'businesses/service_detail.html'

    form_class = BusinessForm

    model = Business


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('businesses:plist')


class ServiceDeleteView(DeleteView, LoginRequiredMixin):
    model = Service
    success_url = reverse_lazy('businesses:slist')
