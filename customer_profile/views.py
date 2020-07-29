from django.shortcuts import render
from .models import Contact, Business
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'customer/profile.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    if request.method == 'POST':

        if (request.POST.get('senderName') and 
            request.POST.get('subject') and request.POST.get('description') ):

            post = Contact()
            post.user = request.POST.get('user_email')
            post.name = request.POST.get('senderName')
            post.subject = request.POST.get('subject')
            post.description = request.POST.get('description')
            post.user = request.user

            post.save()

            return render(request, 'confirmation_reg.html')
    else:
            return render(request, 'contact.html')

def postRegisterForm(request):
        if request.method == 'POST':
            if ( request.POST.get('businessName') and request.POST.get('businessType') and 
            request.POST.get('inputProvince') and request.POST.get('inputCity') and
            request.POST.get('inputAddress') and 
             request.POST.get('inputPostalCode') ) :

                post = Business()
                post.name = request.POST.get('businessName')
                post.type = request.POST.get('businessType')
                post.province = request.POST.get('inputProvince')
                post.city = request.POST.get('inputCity')
                post.address = request.POST.get('inputAddress')
                post.address2 = request.POST.get('inputAddress2')
                post.postal_code = request.POST.get('inputPostalCode')
                post.logo = request.POST.get('inputLogo')
                post.user = request.user

                post.save()
                
                return render(request, 'customer/confirmation_reg.html', {'post': post})  

        else:
                return render(request, "customer/register.html")


def manageBusiness(request):

    if request.method == 'POST':
        if request.POST.get('businessSelect'):
            business = request.POST.get('businessSelect')
            options = Business.objects.filter(Q(name__icontains=business))

            return render(request, 'customer/business_manage.html', {'options': options})
    else:
        user_name = request.user
        options = Business.objects.filter(Q(user=user_name))

    return render(request, 'customer/manage.html', {'options': options})

def BusinessAdmin(request):
    # this is effectively replaced by manage business
    user_name = request.user
    options = Business.objects.filter(Q(user=user_name), Q(name__icontains=id))
    
    return render(request, 'customer/business_manage.html', {'options': business})
