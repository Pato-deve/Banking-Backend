from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='transaction_list'),  # Lista de transacciones del usuario
    path('<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),  # Detalle de una transacción específica
    path('create/', views.create_transaction, name='transaction_create'),  # Creación de una nueva transacción
    path('<int:pk>/delete/', views.delete_transaction, name='transaction_delete'),  # Eliminación de una transacción
]