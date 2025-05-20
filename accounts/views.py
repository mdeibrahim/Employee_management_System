from django.shortcuts import render
# accounts/views.py
from django.contrib.auth import get_user_model
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    UserProfileSerializer,
    TokenBlacklistSerializer # Optional
)

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    # CREATE: POST /api/employers/
    # READ: GET /api/employers/
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny] # Anyone can register

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Optionally, generate tokens for the user immediately after registration
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserProfileSerializer(user, context=self.get_serializer_context()).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)


class UserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer # Use our custom serializer


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can see their profile

    def get_object(self):
        return self.request.user # Returns the currently logged-in user


# Optional: Logout View
class UserLogoutView(APIView):
    serializer_class = TokenBlacklistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        except Exception as e: # Catch validation errors or other issues
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

