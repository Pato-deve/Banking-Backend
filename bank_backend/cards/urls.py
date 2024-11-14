from django.urls import path
from . import views

urlpatterns = [
    path('', views.CardListView.as_view(), name='card_list'),
    path('<int:pk>/', views.CardDetailView.as_view(), name='card_detail'),
    path('create/', views.create_card, name='card_create'),
    path('<int:pk>/delete/', views.delete_card, name='card_delete'),
]