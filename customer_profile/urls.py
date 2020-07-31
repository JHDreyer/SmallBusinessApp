from django.urls import path

from . import views
app_name = 'customer_profile'
urlpatterns = [
    path('options/', views.index, name='profile'),
    path('options/login/google/', views.login, name='login'),
    path('options/manage', views.manageBusiness, name='manage'),
    path('options/manage/products', views.manageProducts, name='manage_products'),
    path('contact_us/', views.contact, name='contact'),

    path('create/', views.BusinessCreateView.as_view(), name='create'),

    path('business/list/', views.BusinessListView.as_view(), name='list'),
    path('business/<int:pk>/update/',
         views.BusinessUpdateView.as_view(), name='update'),
    path('business/<int:pk>/delete/',
         views.BusinessDeleteView.as_view(), name='delete'),
]
