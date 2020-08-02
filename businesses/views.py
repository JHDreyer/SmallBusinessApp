from django.shortcuts import HttpResponseRedirect, render, get_object_or_404, redirect
from businesses.models import Business, Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (CreateView, UpdateView, DeleteView, ListView)
from django.urls import reverse_lazy
from .forms import BusinessForm, ProductForm


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


def BusinessListView(request):
    model = Business()
    businesses = Business.objects.filter(user=request.user)
    return render(request, 'businesses/business_list.html', {'businesses': businesses})


def ProductListView(request):
    name = request.GET.get('viewProducts')
    products = Product.objects.filter(business=name)
    return render(request, 'businesses/product_list.html', {'product_list': product_list})


@login_required
def ProductCreateView(request, pk):
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


# newwwwwwwww
"""def ProductList(request, ):
    product_list = Product.objects.all()
    return render(request, 'businesses/product_list.html', {'product_list': product_list})"""


def ProductUpdateView(request, pk):

    context = {}
    obj = get_object_or_404(Product, pk=pk)

    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return render(request, 'business/profile.html')

    context["form"] = form

    return render(request, "businesses/product_update.html", context)


def ProductDeleteView(request, pk):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        obj.delete()
        return render(request, 'business/profile.html')

    return render(request, "businesses/product_confirm_delete.html", context)
