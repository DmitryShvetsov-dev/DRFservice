from django.contrib import admin
from django.urls import path, include
from products.views import OrdersViewSet
from subscriptions.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"tariff", TariffViewSet)
router.register(r"order", OrdersViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/usersubscribtion/<int:pk>/", UserSubscriptionsDetailView.as_view()),
]
