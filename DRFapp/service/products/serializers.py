from rest_framework import serializers
from users.models import CustomUser
from products.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all()) 

    class Meta:
        model = Orders
        fields = "__all__"
