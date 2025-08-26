from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import RedirectView
from users.views import RegisterView, UserProfileView, CustomLoginView, home
from activities.views import ActivityListCreateView, ActivityDetailView, ActivitySummaryView
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Landing page
    path('', home, name='home'), 
    
    # Optional: redirect /api/ to landing page
    path('api/', RedirectView.as_view(url='/', permanent=False)),

    # Registration
    # path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/register/', csrf_exempt(RegisterView.as_view()), name='register'),

    # User profile
    path('api/auth/profile/', UserProfileView.as_view(), name='user-profile'),

    # Activities
    path('api/activities/', ActivityListCreateView.as_view(), name='activities_list_create'),
    path('api/activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),

    # JWT token endpoints
    # path('api/auth/login/', CustomLoginView.as_view(), name='login'),
    path('api/auth/login/', csrf_exempt(CustomLoginView.as_view()), name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Activity summary
    path('api/activities/summary/', ActivitySummaryView.as_view(), name='activities_summary'),
]
