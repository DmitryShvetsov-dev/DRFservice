from users.models import CustomUser
from products.models import Orders
from products.serializers import OrdersSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import requests
import os


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


def send_notification(telegram_id, message):
    token = os.environ.get("TELEGRAM_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    json_req = {"chat_id": telegram_id, "text": message}
    requests.post(url, json=json_req)
