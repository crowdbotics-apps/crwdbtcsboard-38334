import token

from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        request_token = Token.objects.filter(key=request.auth).first()
        if not request_token:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(request_token.user)
        return Response(status=HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, *args, pk=None):
        request_token = Token.objects.filter(key=request.auth).first()
        if not request_token:
            return Response(status=HTTP_404_NOT_FOUND)
        queryset = request_token.user.subscription_user.filter(pk=pk).first()
        data = {
            "name": request_token.user.name,
            "email": request_token.user.email,
            "subscription": [
                {
                    "id":queryset.app.pk,
                    "name":queryset.app.description,
                    "description":queryset.app.description,
                    "domain":queryset.app.domain_name,
                    "framework":queryset.app.framework,
                }
            ]
        }
        return Response(status=HTTP_200_OK, data=data)