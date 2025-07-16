from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import TokenError


from .serializers import LoginSerializer, TokenRefreshSerializer, UserSerializer


class PhoneLoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data.get("phone_number")
        password = serializer.validated_data.get("password")

        user = authenticate(request, username=phone_number, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            refresh["schema"] = user.school.name if user.school else "public"

            serializer = UserSerializer(user, context={"request": request})

            return Response({"refresh": str(refresh), "access": str(refresh.access_token), "user": serializer.data})

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class RefreshTokenAPIView(GenericAPIView):
    serializer_class = TokenRefreshSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data.get("refresh")

        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            schema = refresh.get("schema", None)
            role = refresh.get("role", None)
            full_name = refresh.get("full_name", None)

            return Response(
                {
                    "access": access_token,
                    "schema": schema,
                    "role": role,
                    "full_name": full_name,
                }
            )

        except TokenError:
            return Response({"detail": "Token yaroqsiz yoki muddati tugagan"}, status=status.HTTP_401_UNAUTHORIZED)


class WhoAmIAPIView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
