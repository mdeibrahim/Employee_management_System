from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')), # This is the base for your auth endpoints
    # Include the employer URLs from the 'employers' app.
    # This will handle endpoints like /api/employers/ and /api/employers/<id>/
    path('api/employers/', include('employers.urls')),

    # Simple JWT token endpoints (if you haven't included them in accounts.urls)
    # If you already have these in accounts.urls, you can remove them here.
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
