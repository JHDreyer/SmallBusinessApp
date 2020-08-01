from django.shortcuts import render
from django.http import HttpResponse 
from . models import Platforms

def advertising(request):
    return render(request, 'advertising.html')


def ad_signUp(request):

    if request.method == 'POST':

        if (request.POST.get('facebook') and request.POST.get('instagram') and 
            request.POST.get('google') and request.POST.get('budgetperiod') and 
            request.POST.get('budget') and request.POST.get('extraInfo') ):

            application = Platforms()
            #post.user = request.user
            application.facebook = request.POST.get('facebook')
            application.instagram = request.POST.get('instagram')
            application.google = request.POST.get('google')
            application.budget = request.POST.get('budget')
            application.budgetperiod = request.POST.get('budgetperiod')
            application.extrainfo = request.POST.get('extraInfo')
            #post.businessname = request.POST.get('')

            application.save()

            return render(request, 'confirmation_contact.html')
    else:
        return render(request, 'application.html')


