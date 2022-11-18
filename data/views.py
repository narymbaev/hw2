from django.shortcuts import render, redirect
from .models import *
from .forms import *


# DISEASE-TYPE
def diseaseType(request):
    disease_type = DiseaseType.objects.all()
    context = {'disease_type': disease_type}
    return render(request, 'read/disease_type.html', context)

def createDiseaseType(request):
    form = DiseaseTypeForm()
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease-type')
        
    pass

def deleteDiseaseType(request, id):
    disease_type = DiseaseType.objects.get(id=id)
    if request.method == 'POST':
        disease_type.delete()
        return redirect('disease-type')

#COUNTRY
def country(request):
    country = Country.objects.all()
    context = {'country': country}
    return render(request, 'read/country.html', context)

def deleteCountry(request, cname):
    country = Country.objects.get(cname=cname)
    if request.method == 'POST':
        country.delete()
        return redirect('country')

# DISEASE
def disease(request):
    disease = Disease.objects.all()
    context = {'disease': disease}
    return render(request, 'read/disease.html', context)

def deleteDisease(request, disease_code):
    disease = Disease.objects.get(disease_code=disease_code)
    if request.method == 'POST':
        disease.delete()
        return redirect('disease')

#DISCOVER
def discover(request):
    discover = Discover.objects.all()
    context = {'discover': discover}
    return render(request, 'read/discover.html', context)

def deleteDiscover(request, id):
    discover = Discover.objects.get(id=id)
    if request.method == 'POST':
        discover.delete()
        return redirect('discover')

#USERS
def users(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'read/user.html', context)

def deleteUsers(request, email):
    user = Users.objects.get(email=email)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request, 'delete/delete-user.html')

#PUBLIC_SERVANT
def publicServant(request):
    public_servants = PublicServant.objects.all()
    context = {'public_servants': public_servants}
    return render(request, 'read/public_servant.html', context)

def deletePublicServant(request, email_id):
    public_servant = PublicServant.objects.get(email_id=email_id)
    if request.method == 'POST':
        public_servant.delete()
        return redirect('public-servant')

#DOCTOR
def doctor(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'read/doctor.html', context)

def deleteDoctor(request, email_id):
    doctor = Doctor.objects.get(email_id=email_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor')

#SPECIALIZE
def specialize(request):
    specializes = Specialize.objects.all()
    context = {'specializes': specializes}
    return render(request, 'read/specialize.html', context)

def deleteSpecialize(request, id):
    specialize = Specialize.objects.get(id=id)
    if request.method == 'POST':
        specialize.delete()
        return redirect('specialize')

#RECORD
def record(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'read/record.html', context)

def deleteRecord(request, id):
    record = Record.objects.get(id=id)
    if request.method == 'POST':
        record.delete()
        return redirect('record')