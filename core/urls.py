from django.urls import path
from users.views import RegisterView, UserProfileView, CustomLoginView
from activities.views import ActivityListCreateView, ActivityDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Registration
    path('api/auth/register/', RegisterView.as_view(), name='register'),

    # User profile
    path('api/auth/profile/', UserProfileView.as_view(), name='user-profile'),

    # Activities
    path('api/activities/', ActivityListCreateView.as_view(), name='activities_list_create'),
    path('api/activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),

    # JWT token endpoints
    path('api/auth/login/', CustomLoginView.as_view(), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
