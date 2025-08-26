from django.urls import path
from django.shortcuts import redirect
from users.views import RegisterView, UserProfileView, CustomLoginView, api_home, home
from activities.views import ActivityListCreateView, ActivityDetailView, ActivitySummaryView
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib import admin

# Redirect /api/ to the homepage
def api_root_redirect(request):
    return redirect('/')  # Redirects to your home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # /api/ root redirect
    path('api/', api_home, name='api-home'),


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

    # Activity summary
    path('api/activities/summary/', ActivitySummaryView.as_view(), name='activities_summary'),
]
