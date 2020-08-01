from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'businesses'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='business/profile.html'), name='profile'),

    path('manage/', views.manageBusiness, name='manage'),


    path('business/create/', views.BusinessCreateView.as_view(), name='bcreate'),
    path('business/list/', views.BusinessListView, name='blist'),
     path('business/list/products', views.ProductListView, name='product_list'),

    path('business/<int:pk>/update/',
         views.BusinessUpdateView.as_view(), name='bupdate'),
    path('business/<int:pk>/delete/',
         views.BusinessDeleteView.as_view(), name='bdelete'),

    path('<int:pk>/product/',
         views.add_product_to_business, name='pcreate'),
    #path('product/list/', views.ProductListView, name='plist'),
    path('product/<int:pk>/update/',
         views.ProductUpdateView.as_view(), name='pupdate'),
    path('product/<int:pk>/delete/',
         views.ProductDeleteView.as_view(), name='pdelete'),
]
