from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('walking', 'Walking'),
        ('swimming', 'Swimming'),
        ('other', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"
