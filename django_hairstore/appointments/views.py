# appointments/views.py
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required

# Render the homepage
def get_homepage(request):
    return render(request, 'appointments/homepage.html')

# Handle appointment booking
@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('homepage')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})
