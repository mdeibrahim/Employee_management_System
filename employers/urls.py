from django.urls import path
from .views import EmployerListCreateView, EmployerDetailView

# Define app_name for namespacing URLs.
app_name = 'employers'

urlpatterns = [
    # URL pattern for listing and creating employers.
    path('', EmployerListCreateView.as_view(), name='employer-list-create'),

    # URL pattern for retrieving, updating, and deleting a specific employer.
    path('<int:pk>/', EmployerDetailView.as_view(), name='employer-detail'),
]

