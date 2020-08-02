from django.urls import path

from . import views

app_name = 'explore'

urlpatterns = [

    path('', views.explore, name='explore'),
    path('search/', views.search, name='search_results'),
    path('search/business/<int:pk>/',
         views.BusinessDetailView, name='business_detail'),
    path('about/', views.about, name='about'),
    path('search/product/<int:pk>/<slug:slug>/',
         views.ProductDetailView, name='product_detail'),


]
