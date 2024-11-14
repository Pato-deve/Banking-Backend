from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoanListView.as_view(), name='loan_list'),
    path('<int:pk>/', views.LoanDetailView.as_view(), name='loan_detail'),
    path('create/', views.create_loan, name='loan_create'),
    path('<int:pk>/delete/', views.delete_loan, name='loan_delete'),
]