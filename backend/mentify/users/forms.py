from django import forms
from .models import Doctor,Booking,Appointment,Prescription
class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'