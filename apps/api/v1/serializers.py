from rest_framework import serializers
from apps.models import Application

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"