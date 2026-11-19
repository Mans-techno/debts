from django.urls import path
from .views import ShopListCreateView, ShopDetailView, DebtsListCreateView, DebtDetailView


urlpatterns = [
    path('shops/', ShopListCreateView.as_view(), name='shop_list_create'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop_detail'),
    path('', DebtsListCreateView.as_view(), name='debts_list_create'),
    path('<int:pk>/', DebtDetailView.as_view(), name='debt_detail'),
]
