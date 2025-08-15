from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer

# List and create activities for the logged-in user
class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return activities of the logged-in user
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the logged-in user
        serializer.save(user=self.request.user)

# Retrieve, update, delete a single activity (user can only modify their own)
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow access to the logged-in user's activities
        return Activity.objects.filter(user=self.request.user)
