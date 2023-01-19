from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from subscriptions.models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework import viewsets
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from rest_framework.response import Response


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Subscription.objects.all()

    def destroy(self, request, *args, **kwargs):
        subscription_id = kwargs.get("pk", None)

        if not subscription_id:
            return Response(status=HTTP_404_NOT_FOUND)

        subscription = Subscription.objects.filter(id=subscription_id, active=True).first()

        if not subscription:
            return Response(status=HTTP_404_NOT_FOUND)

        subscription.active = False
        subscription.save()

        return Response(status=HTTP_204_NO_CONTENT)
