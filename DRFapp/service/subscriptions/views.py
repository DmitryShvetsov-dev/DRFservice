from subscriptions.models import Tariff, UserSubscription
from subscriptions.serializers import TariffSerializer, UserSubscriptionSerializer
from rest_framework import generics, viewsets

# CRUD для тарифов
class TariffViewSet(viewsets.ModelViewSet):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


# только GET с idшником
class UserSubscriptionsDetailView(generics.RetrieveAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
