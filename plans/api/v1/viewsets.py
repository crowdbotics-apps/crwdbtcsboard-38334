from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from plans.models import Plan
from .serializers import PlanSerializer
from rest_framework import viewsets

class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Plan.objects.all()