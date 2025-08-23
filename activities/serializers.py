from rest_framework import serializers
from django.utils import timezone
from .models import Activity

# Serializer for activity summary
class ActivitySummarySerializer(serializers.Serializer):
    total_calories = serializers.IntegerField()
    total_distance = serializers.FloatField()
    total_duration = serializers.IntegerField()

# Dynamic ChoiceField to show allowed types in error message
class DynamicChoiceField(serializers.ChoiceField):
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError:
            allowed = ', '.join(str(choice) for choice in self.choices.keys())
            raise serializers.ValidationError(
                f"Invalid activity type. Allowed types are: {allowed}."
            )

# Main serializer for Activity model
class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    # Dynamic activity_type field
    activity_type = DynamicChoiceField(
        choices=Activity._meta.get_field('activity_type').choices
    )

    # Field-level validations with custom messages
    duration_minutes = serializers.IntegerField(
        min_value=1,
        max_value=1440,
        error_messages={
            "min_value": "Duration must be at least 1 minute.",
            "max_value": "Duration cannot exceed 1440 minutes (24 hours)."
        }
    )
    distance_km = serializers.FloatField(
        required=False,
        allow_null=True,
        min_value=0.0,
        error_messages={
            "min_value": "Distance must be a positive number."
        }
    )
    calories_burned = serializers.IntegerField(
        min_value=0,
        max_value=100000,
        error_messages={
            "min_value": "Calories burned cannot be negative.",
            "max_value": "Calories burned exceeds the maximum realistic value."
        }
    )

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
            'notes',
        ]

    def validate(self, attrs):
        """
        Cross-field/business rules:
        - distance_km is required and > 0 for distance-based activities
        - date cannot be in the future
        """
        # Support partial updates
        activity_type = attrs.get('activity_type') or getattr(self.instance, 'activity_type', None)
        distance_km = attrs.get('distance_km', getattr(self.instance, 'distance_km', None))
        date = attrs.get('date', getattr(self.instance, 'date', None))

        # Distance-required types dynamically from model choices
        distance_required_types = {
            choice[0] for choice in Activity._meta.get_field('activity_type').choices
            if choice[0] in {'running', 'cycling', 'walking', 'swimming'}
        }

        if activity_type in distance_required_types:
            if distance_km in (None, ''):
                raise serializers.ValidationError({
                    'distance_km': f"Distance is required for {activity_type} activities."
                })
            if float(distance_km) <= 0.0:
                raise serializers.ValidationError({
                    'distance_km': f"Distance must be greater than 0 for {activity_type} activities."
                })

        # No future dates allowed
        if date and date > timezone.localdate():
            raise serializers.ValidationError({
                'date': "Activity date cannot be in the future."
            })

        return attrs

    def create(self, validated_data):
        # The view will pass user via serializer.save(user=request.user)
        return Activity.objects.create(**validated_data)
