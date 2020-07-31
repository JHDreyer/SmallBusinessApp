from django.urls import path

from . import views


urlpatterns = [

    path('', views.advertising, name='advertising'),
    path('signUpForAds/', views.ad_signUp, name='signUpForAds')
    
]

