from rest_framework import serializers
from users.models import User
from subscriptions.api.v1.serializers import UserSubscriptionSerializer


class UserSerializer(serializers.ModelSerializer):
    subscription_user = UserSubscriptionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["name", "email", "subscription_user"]
