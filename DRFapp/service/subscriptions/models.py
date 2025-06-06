from django.db import models
from django.core.validators import MaxValueValidator
from users.models import CustomUser


class Tariff(models.Model):
    tariff_type = models.CharField(max_length=20)
    discount_percent = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.tariff_type} id:{self.id}"


class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT)

    def __str__(self):
        return f"(id{self.id}) Client: {self.user} have {self.tariff}"
