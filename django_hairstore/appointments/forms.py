# appointments/forms.py

from django import forms
from .models import Appointment, Service

TIME_CHOICES = [
    ('09:00', '09:00 AM'),
    ('10:00', '10:00 AM'),
    ('11:00', '11:00 AM'),
    ('12:00', '12:00 PM'),
    ('13:00', '01:00 PM'),
    ('14:00', '02:00 PM'),
    ('15:00', '03:00 PM'),
    ('16:00', '04:00 PM'),
    ('17:00', '05:00 PM')
]

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Date',
    )
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        label='Time',
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(), 
        label="Select Service"
    )

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'service', 'notes']
