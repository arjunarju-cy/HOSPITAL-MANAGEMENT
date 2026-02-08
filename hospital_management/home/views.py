from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from .models import Department, Doctor
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            subject = f'New Appointment Booking - {booking.p_name}'
            message = f'''
       A new booking has been made:

       Name: {booking.p_name}
       Phone: {booking.p_phone}
       Email: {booking.p_email}
       Doctor: {booking.doc_name}
       Date: {booking.booking_date}
       Booked On: {booking.booked_on}
            '''

            send_mail(
                subject,
                message,
                'your-email@gmail.com',
                ['recipient-email@example.com'],
                fail_silently=False,
        )

            return render(request, 'confirmation.html')
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')

def department(request):
    return render(request, 'department.html', {
        'dept': Department.objects.all()
    })

def doctor(request):
    return render(request, 'doctor.html', {
        'doctors': Doctor.objects.all()
    })

