from rest_framework import serializers
from .models import Debts, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debts
        fields = '__all__'
        
