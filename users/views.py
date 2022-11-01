from django.contrib.auth import authenticate

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView, Request, Response, status
from rest_framework.authtoken.models import Token

from .models import User
from .serializers import UserSerializer, UserPostSerializer, LoginSerializer


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                }
            )

        return Response(
            {"detail": "invalid username or password"},
            status.HTTP_400_BAD_REQUEST,
        )
