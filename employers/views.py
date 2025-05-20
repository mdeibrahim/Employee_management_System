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
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Authentication credentials were not provided.")
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific employer instance.
    - GET: read_Retrieve a specific employer.
    - PUT: Update a specific employer.
    - DELETE: Delete a specific employer.
    """
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # The lookup field is 'pk' by default, but explicitly setting it can improve clarity.
    lookup_field = 'pk' # Assumes the URL pattern uses <int:pk>

