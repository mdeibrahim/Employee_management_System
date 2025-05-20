from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Employer
from .serializers import EmployerSerializer
from .permissions import IsOwner
from rest_framework.exceptions import PermissionDenied

class EmployerListCreateView(generics.ListCreateAPIView):
    """
    API view to list all employers for the authenticated user or create a new employer.
    - GET: List all employers owned by the requesting user.
    - POST: Create a new employer linked to the requesting user.
    """
    serializer_class = EmployerSerializer
    # Require authentication for this view.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Override get_queryset to return only employers owned by the authenticated user.
        """
        # Ensure the user is authenticated before filtering the queryset.
        if not self.request.user.is_authenticated:
             # This case should ideally be handled by permission_classes,
             # but it's a good safeguard.
            raise PermissionDenied("Authentication credentials were not provided.")
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Override perform_create to automatically link the new employer to the authenticated user.
        """
        # Save the serializer with the user set to the requesting user.
        serializer.save(user=self.request.user)


class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific employer instance.
    - GET: Retrieve a specific employer.
    - PUT: Update a specific employer.
    - DELETE: Delete a specific employer.
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    # Require authentication and the custom IsOwner permission.
    # IsAuthenticated ensures the user is logged in.
    # IsOwner ensures the user owns the specific employer instance they are trying to access.
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # The lookup field is 'pk' by default, but explicitly setting it can improve clarity.
    lookup_field = 'pk' # Assumes the URL pattern uses <int:pk>

