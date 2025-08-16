from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Activity
from .serializers import ActivitySerializer


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
    
    # def perform_create(self, serializer):
    #     """
    #     Automatically set the user to the currently authenticated user when creating an activity.
    #     """
    #     serializer.save(user=self.request.user)

# Retrieve, update, and delete a single activity
class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Ensure users can only access their own activities.
        """
        return Activity.objects.filter(user=self.request.user)
