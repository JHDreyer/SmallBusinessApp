from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.index, name='profile'),

    path('manage/', views.manageBusiness, name='manage'),

    path('manage/products/', views.manageProducts, name='manage_products'),

    path('create/', views.BusinessCreateView.as_view(), name='create'),

    path('list/', views.BusinessListView.as_view(), name='list'),
    path('<int:pk>/update/',
         views.BusinessUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',
         views.BusinessDeleteView.as_view(), name='delete'),
]
