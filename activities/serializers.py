from rest_framework import serializers
from .models import Activity  # assuming these are your models

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name', 'description']  # adjust fields based on your model

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    activity_type = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all()
    )

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories', 'date']

    def create(self, validated_data):
        # assign the current logged-in user automatically
        user = self.context['request'].user
        activity = Activity.objects.create(user=user, **validated_data)
        return activity
