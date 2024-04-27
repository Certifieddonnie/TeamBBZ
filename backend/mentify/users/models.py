from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Doctor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100)
    experience=models.IntegerField()
    qualification=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
class Patient(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    def __str__(self):
        return self.user.username
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return self.doctor.user.username

class Prescription(models.Model):
    appointment=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    prescription=models.TextField()
    def __str__(self):
        return self.appointment.doctor.user.username

class Booking(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    def __str__(self):
        return self.doctor.user.username
