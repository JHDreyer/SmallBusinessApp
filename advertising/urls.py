from django.urls import path

from . import views


app_name = 'advertising'

urlpatterns = [

    path('', views.advertising, name='advertising'),
    path('signUpForAds/', views.ad_signUp, name='signUpForAds')

]
