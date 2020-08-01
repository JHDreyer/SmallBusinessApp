from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'businesses'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='business/profile.html'), name='profile'),

    path('manage/', views.manageBusiness, name='manage'),


    path('business/create/', views.BusinessCreateView.as_view(), name='bcreate'),
    path('business/list/', views.BusinessListView.as_view(), name='blist'),
    path('business/<int:pk>/update/',
         views.BusinessUpdateView.as_view(), name='bupdate'),
    path('business/<int:pk>/delete/',
         views.BusinessDeleteView.as_view(), name='bdelete'),

    path('product/create/', views.ProductCreateView.as_view(), name='pcreate'),
    #     path('product/list/', views.BusinessListView.as_view(), name='plist'),
    #     path('product/<int:pk>/update/',
    #          views.BusinessUpdateView.as_view(), name='pupdate'),
    #     path('product/<int:pk>/delete/',
    #          views.BusinessDeleteView.as_view(), name='pdelete'),

    path('service/create/', views.ServiceCreateView.as_view(), name='screate'),
    #     path('service/list/', views.BusinessListView.as_view(), name='slist'),
    #     path('service/<int:pk>/update/',
    #          views.BusinessUpdateView.as_view(), name='supdate'),
    #     path('service/<int:pk>/delete/',
    #          views.BusinessDeleteView.as_view(), name='sdelete'),


]
