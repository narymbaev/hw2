from django.shortcuts import render
from .models import DiseaseType, Country, Disease, Discover, Users, PublicServant, Doctor, Specialize, Record 

# Create your views here.
def diseaseType(request):
    disease_type = DiseaseType.objects.all()
    context = {'disease_type': disease_type}
    return render(request, 'disease_type.html', context)

def country(request):
    country = Country.objects.all()
    context = {'country': country}
    return render(request, 'country.html', context)

def disease(request):
    disease = Disease.objects.all()
    context = {'disease': disease}
    return render(request, 'disease.html', context)

def discover(request):
    discover = Discover.objects.all()
    context = {'discover': discover}
    return render(request, 'discover.html', context)

def users(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'user.html', context)

def publicServant(request):
    public_servants = PublicServant.objects.all()
    context = {'public_servants': public_servants}
    return render(request, 'public_servant.html', context)

def doctor(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor.html', context)

def specialize(request):
    specializes = Specialize.objects.all()
    context = {'specializes': specializes}
    return render(request, 'specialize.html', context)

def record(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'record.html', context)