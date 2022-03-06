from django.conf.urls import url
from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investor_list', views.investor_list, name='investor_list'),
    path('investor/create/', views.investor_new, name='investor_new'),
    path('investor/<int:pk>/edit/', views.investor_edit, name='investor_edit'),
    path('investor/<int:pk>/delete/', views.investor_delete, name='investor_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    url(r'^customers_json/', views.CustomerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)