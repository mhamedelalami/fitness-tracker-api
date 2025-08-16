from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # user is read-only

    class Meta:
        model = Activity
        fields = [
            'id',
            'user',
            'activity_type',
            'duration_minutes',
            'distance_km',
            'calories_burned',
            'date',
            'notes'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return Activity.objects.create(user=user, **validated_data)
