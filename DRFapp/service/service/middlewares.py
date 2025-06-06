from subscriptions.models import UserSubscription
from rest_framework.exceptions import PermissionDenied

class SubscriptionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "/api/order/" in request.path:
            self.user_have_active_subscription(request.user)
        response = self.get_response(request)
        return response

    def user_have_active_subscription(self, user):
        try:
            subscription = UserSubscription.objects.get(user=user)
            if subscription:
                return True
        except:
            raise PermissionDenied("error : User dont have active subscription")  # тут для демонстрации поствил отклонение запроса, но в реальном проекте тут нужно сделать редирект на страницу подписки