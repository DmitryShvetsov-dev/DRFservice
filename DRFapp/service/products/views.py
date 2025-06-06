from products.models import Orders
from products.serializers import OrdersSerializer
from rest_framework import viewsets

# CRUD для заказов
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer