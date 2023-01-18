from rest_framework import authentication
from applications.models import Application
from .serializers import ApplicationSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Application.objects.all()