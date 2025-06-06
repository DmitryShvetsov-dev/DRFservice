from users.models import CustomUser
from products.models import Orders
from products.serializers import OrdersSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from products.tgnotify import send_notification

# CRUD для заказов + дополнительная логика для POST чтобы бот присылал уведомление
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    
    
    def perform_create(self, serializer):
        order = serializer.save()
        user = get_object_or_404(CustomUser, id=order.user_id)
        if user.telegram_id:
            send_notification(
                user.telegram_id, f"Вам пришёл новый заказ: {order.product}"
            )
