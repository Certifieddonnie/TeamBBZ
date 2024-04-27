from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from .models import Doctor,Booking,Appointment,Prescription
import pickle
import pandas as pd
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phoneno=request.POST['phone_number']
        city=request.POST['city']
        state=request.POST['state']
    User.objects.create(username=username,password=password,email=email,phoneno=phoneno,city=city,state=state)
    return redirect('home')
    return render(request,'register.html')
def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=='POST':
        usename=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('success')
        return render(request,'login.html')

def Doctor(request):
    user=request.user()
    if Doctor.Objects.filter(user=user).exists():
        role='Doctor'
    
    else:
        role='Uknnown'
    return render(request,'doctor-registration.html')

def Patient(request):
    user=request.user()
    if Patient.Objects.filter(user=user).exists():
        role='patient'
    else:
        role='Uknowkm'
    return render(request,'patient-registration.html')

def make_appointment(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appoitment_sucess')
    else:
        form=ApointmentForm()
    return render(request,'make_appointment.html',{'form':form})

def view_appointment(request):
    appointment=Appointment.objects.all()
    return render(request,'view_appointment.html',{'appointment':appointment})

def make_booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_sucess')
    else:
        form=BookingForm()
    return render(request,'make_booking.html',{'form':form})

def view_booking(request):
    booking=Booking.objects.all()
    return render(request,'view_booking.html',{'booking':booking})

def make_prescription(request):
    prescribe=Prescription.objects.all()
    return render(request,'make_prescription.html',{'prescribe':prescribe})

def view_prescription(request):
    prescription=Prescription.objects.all()
    return render(request,'view_prescription.html',{'prescription':prescription})

def prediction(request):
    with open('model.pkl','rb') as f:
        model=pickle.load(f)
    data=request.GET.get('data')
    pd_data=pd.DataFrame(eval(data))
    result=model.predict(pd_data)
    return render(request,'prediction.html',{'result':result})

