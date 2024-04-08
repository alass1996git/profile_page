from django.contrib.auth.models import User
from rest_framework import serializers
from .models import menuModel
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menuModel
        fields = ['ID2', 'Title', 'Price', 'Inventory']