from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name='customer_list'),
    path('detail/', views.customer_detail, name='customer_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='customers/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]