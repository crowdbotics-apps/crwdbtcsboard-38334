from rest_framework import serializers
from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):
    app = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()
    class Meta:
        model = Subscription
        fields = ["plan", "app", "active"]

    def get_app(self, obj):
        return obj.app.name

    def get_plan(self,obj):
        return obj.plan.name
