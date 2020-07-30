from django.urls import path

from . import views

urlpatterns = [
    path('options/', views.index, name='profile'),
    path('options/register/', views.postRegisterForm, name='register'),
    path('options/login/google/', views.login, name='login'),
    path('options/manage', views.manageBusiness, name='manage'),
    path('options/manage/products', views.manageProducts, name='manage_products'),
    path('contact_us/', views.contact, name='contact'),  
]