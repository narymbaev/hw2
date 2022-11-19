from django.shortcuts import render, redirect
from .models import *
from .forms import *


def welcome(request):
    return render(request, 'welcome.html')

# DISEASE-TYPE
def diseaseType(request):
    disease_types = DiseaseType.objects.all()
    context = {'disease_types': disease_types}
    return render(request, 'read/disease_type.html', context)

def createDiseaseType(request):
    form = DiseaseTypeForm()
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease-type')
    context = {"form": form}
    return render(request, 'create/disease_type.html', context)

def updateDiseaseType(request, id):
    disease_type = DiseaseType.objects.get(id=id)
    form = DiseaseTypeForm(instance=disease_type)
    context = {'form': form}
    if request.method == 'POST':
        form = DiseaseTypeForm(request.POST, instance=disease_type)
        if form.is_valid():
            form.save()
            return redirect('disease-type')
    return render(request, 'update/disease_type.html', context)

def deleteDiseaseType(request, id):
    disease_type = DiseaseType.objects.get(id=id)
    disease_type.delete()
    return redirect('disease-type')

#COUNTRY
def country(request):
    country = Country.objects.all()
    context = {'countries': country}
    return render(request, 'read/country.html', context)

def createCountry(request):
    form = CountryForm()
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country')
    context = {"form": form}
    return render(request, 'create/country.html', context)

def updateCountry(request, id):
    country = Country.objects.get(id=id)
    form = CountryForm(instance=country)
    context = {'form': form}
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country')
    return render(request, 'update/country.html', context)    

def deleteCountry(request, id):
    country = Country.objects.get(id=id)
    country.delete()
    return redirect('country')

# DISEASE
def disease(request):
    diseases = Disease.objects.all()
    context = {'diseases': diseases}
    return render(request, 'read/disease.html', context)

def createDisease(request):
    form = DiseaseForm()
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disease')
    context = {"form": form}
    return render(request, 'create/disease.html', context)

def updateDisease(request, id):
    disease = Disease.objects.get(id=id)
    form = DiseaseForm(instance=disease)
    context = {'form': form}
    if request.method == 'POST':
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('disease')
    return render(request, 'update/disease.html', context)

def deleteDisease(request, id):
    disease = Disease.objects.get(id=id)
    disease.delete()
    return redirect('disease')

#DISCOVER
def discover(request):
    discovers = Discover.objects.all()
    context = {'discovers': discovers}
    return render(request, 'read/discover.html', context)

def createDiscover(request):
    form = DiscoverForm()
    if request.method == 'POST':
        form = DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discover')
    context = {"form": form}
    return render(request, 'create/discover.html', context)

def updateDiscover(request, id):
    discover = Discover.objects.get(id=id)
    form = DiscoverForm(instance=discover)
    context = {'form': form}
    if request.method == 'POST':
        form = DiscoverForm(request.POST, instance=discover)
        if form.is_valid():
            form.save()
            return redirect('discover')
    return render(request, 'update/discover.html', context)

def deleteDiscover(request, id):
    discover = Discover.objects.get(id=id)
    discover.delete()
    return redirect('discover')

#USERS
def users(request):
    users = Users.objects.all()
    context = {'users': users}
    return render(request, 'read/user.html', context)

def createUsers(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {"form": form}
    return render(request, 'create/user.html', context)

def updateUsers(request, id):
    user = Users.objects.get(id=id)
    form = UsersForm(instance=user)
    context = {'form': form}
    if request.method == 'POST':
        form = UsersForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    return render(request, 'update/user.html', context)

def deleteUsers(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('users')

#PUBLIC_SERVANT
def publicServant(request):
    public_servants = PublicServant.objects.all()
    context = {'public_servants': public_servants}
    return render(request, 'read/public_servant.html', context)

def createPublicServant(request):
    form = PublicServantForm()
    free_users = Users.objects.all()
    lst = list()
    # this sheet of code for getting list of free users who is not Doctor nor PublicServant
    for user in free_users:
        if not (Doctor.objects.filter(id=user.id).exists() or PublicServant.objects.filter(id=user.id).exists()):
            lst.append(user)
    if request.method == 'POST':
        email = request.POST.get('user_email')
        form = PublicServantForm(request.POST)
        if form.is_valid():
            public_servant = form.save(commit=False)
            user = Users.objects.get(email=email)
            public_servant.email = user
            public_servant.save()
            return redirect('public-servant')
    context = {"form": form, 'users': lst}
    return render(request, 'create/public_servant.html', context)

def updatePublicServant(request, id):
    public_servant = PublicServant.objects.get(id=id)
    form = PublicServantForm(instance=public_servant)
    context = {'form': form}
    if request.method == 'POST':
        form = PublicServantForm(request.POST, instance=public_servant)
        if form.is_valid():
            form.save()
            return redirect('public-servant')
    return render(request, 'update/public_servant.html', context)

def deletePublicServant(request, id):
    public_servant = PublicServant.objects.get(id=id)
    public_servant.delete()
    return redirect('public-servant')

#DOCTOR
def doctor(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'read/doctor.html', context)

def createDoctor(request):
    form = DoctorForm()
    free_users = Users.objects.all()
    lst = list()
    # this sheet of code for getting list of free users who is not Doctor nor PublicServant
    for user in free_users:
        if not (Doctor.objects.filter(id=user.id).exists() or PublicServant.objects.filter(id=user.id).exists()):
            lst.append(user)

    if request.method == 'POST':
        email = request.POST.get('user_email')
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            user = Users.objects.get(email=email)
            doctor.email = user
            doctor.save()
            return redirect('doctor')
    context = {"form": form, 'users': lst}
    return render(request, 'create/doctor.html', context)

def updateDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorForm(instance=doctor)
    print(form)
    context = {'form': form}
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor')
    return render(request, 'update/doctor.html', context)

def deleteDoctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctor')

#SPECIALIZE
def specialize(request):
    specializes = Specialize.objects.all()
    context = {'specializes': specializes}
    return render(request, 'read/specialize.html', context)

def createSpecialize(request):
    form = SpecializeForm()
    if request.method == 'POST':
        form = SpecializeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialize')
    context = {"form": form}
    return render(request, 'create/specialize.html', context)

def updateSpecialize(request, id):
    specialize = Specialize.objects.get(id=id)
    form = SpecializeForm(instance=specialize)
    context = {'form': form}
    if request.method == 'POST':
        form = SpecializeForm(request.POST, instance=specialize)
        if form.is_valid():
            form.save()
            return redirect('specialize')
    return render(request, 'update/specialize.html', context)

def deleteSpecialize(request, id):
    specialize = Specialize.objects.get(id=id)
    specialize.delete()
    return redirect('specialize')

#RECORD
def record(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'read/record.html', context)

def createRecord(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('record')
    context = {"form": form}
    return render(request, 'create/record.html', context)

def updateRecord(request, id):
    record = Record.objects.get(id=id)
    form = RecordForm(instance=record)
    context = {'form': form}
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('record')
    return render(request, 'update/record.html', context)

def deleteRecord(request, id):
    record = Record.objects.get(id=id)
    record.delete()
    return redirect('record')