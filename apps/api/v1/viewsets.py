from rest_framework import authentication
from apps.models import Application
from .serializers import ApplicationSerializer
from rest_framework import viewsets

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Application.objects.all()