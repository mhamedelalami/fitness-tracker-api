from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import Activity
from .serializers import ActivitySerializer, ActivitySummarySerializer

# List and create activities for the logged-in user
class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activity_type', 'date']  # enable filtering by type and date

    def get_queryset(self):
        """
        Return only activities that belong to the logged-in user.
        """
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user to the currently authenticated user when creating an activity.
        """
        serializer.save(user=self.request.user)

# Retrieve, update, and delete a single activity
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own activities.
        """
        return Activity.objects.filter(user=self.request.user)

# Activity summary endpoint
class ActivitySummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        summary = Activity.objects.filter(user=user).aggregate(
            total_calories=Sum('calories_burned'),
            total_distance=Sum('distance_km'),
            total_duration=Sum('duration_minutes')
        )

        # Replace None with 0 if user has no activities
        summary = {key: value or 0 for key, value in summary.items()}

        serializer = ActivitySummarySerializer(summary)
        return Response(serializer.data)
