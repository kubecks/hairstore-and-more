# appointments/models.py

from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_appointments')
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    service = models.CharField(max_length=100)  
    notes = models.TextField(blank=True)  
    
    def __str__(self):
        return f"Appointment for {self.user.username} on {self.date} at {self.time}"
