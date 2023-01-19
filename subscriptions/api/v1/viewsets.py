from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()
