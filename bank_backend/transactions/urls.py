from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('new/', views.transaction_create, name='transaction_form'),
    path('<int:pk>/edit/', views.transaction_update, name='transaction_update'),
]
