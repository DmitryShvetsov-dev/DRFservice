from django.db import models
from users.models import CustomUser


class Orders(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.CharField(max_length=50, default="placeholder")
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"OrderID({self.id}):client {self.user} order {self.product} at {self.order_date}"
