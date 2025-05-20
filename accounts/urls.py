from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserProfileView,
    UserRegistrationView,
    UserLoginView,
    UserLogoutView # Optional
)


urlpatterns = [
    
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserRegistrationView.as_view(), name='user-signup'), # [cite: 8]
    path('login/', UserLoginView.as_view(), name='user-login'), # [cite: 8]
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'), # For refreshing access tokens
    path('profile/', UserProfileView.as_view(), name='user-profile'), # [cite: 8]
    path('logout/', UserLogoutView.as_view(), name='user-logout'), # Optional [cite: 5]
] 