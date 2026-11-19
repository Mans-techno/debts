from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Debts, Shop
from .serializers import DebtSerializer, ShopSerializer


class ShopListCreateView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class DebtsListCreateView(ListCreateAPIView):
    serializer_class = DebtSerializer

    def get_queryset(self):
        queryset = Debts.objects.select_related('shop_id').order_by('-created_at')
        shop = self.request.query_params.get('shop')
        if shop:
            queryset = queryset.filter(shop_id=shop)
        return queryset


class DebtDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Debts.objects.all()
    serializer_class = DebtSerializer
