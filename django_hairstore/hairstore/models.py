# hairstore/models.py

from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)

# Define the services offered by the hair salon
class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text='Duration in minutes')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Define the appointment details
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hairstore_appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.name} on {self.date}"
