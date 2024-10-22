# appointments/views.py

from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from datetime import datetime

# Render the homepage
def get_homepage(request):
    return render(request, 'appointments/homepage.html')

# Handle appointment booking - requires login
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            # Combine date and time into a single datetime object
            appointment.date = datetime.combine(date, datetime.strptime(time, "%H:%M").time())
            appointment.user = request.user  # Assign the user directly
            appointment.save()
            return redirect('homepage')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})

# Handle user signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after successful registration
            return redirect('homepage')  # Redirect to the homepage after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# FAQ view
def faq_view(request):
    return render(request, 'appointments/faq.html')