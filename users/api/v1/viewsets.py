from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        user = User.objects.all().first()
        serializer = UserSerializer(user)
        return Response(status=HTTP_200_OK, data=serializer.data)
