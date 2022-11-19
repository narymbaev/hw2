from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    #read
    path('disease-type/', diseaseType, name='disease-type'),
    path('country/', country, name='country'),
    path('disease/', disease, name='disease'),
    path('discover/', discover, name='discover'),
    path('users/', users, name='users'),
    path('public-servant/', publicServant, name='public-servant'),
    path('doctor/', doctor, name='doctor'),
    path('specialize/', specialize, name='specialize'),
    path('record/', record, name='record'),

    #create
    path('disease-type/create/', createDiseaseType, name='create-disease-type'),
    path('country/create/', createCountry, name='create-country'),
    path('disease/create/', createDisease, name='create-disease'),
    path('discover/create/', createDiscover, name='create-discover'),
    path('users/create/', createUsers, name='create-users'),
    path('public-servant/create/', createPublicServant, name='create-public-servant'),
    path('doctor/create/', createDoctor, name='create-doctor'),
    path('specialize/create/', createSpecialize, name='create-specialize'),
    path('record/create/', createRecord, name='create-record'),

    #update
    path('disease-type/update/<int:id>/', updateDiseaseType, name='update-disease-type'),
    path('country/update/<int:id>/', updateCountry, name='update-country'),
    path('disease/update/<int:id>/', updateDisease, name='update-disease'),
    path('discover/update/<int:id>/', updateDiscover, name='update-discover'),
    path('users/update/<int:id>/', updateUsers, name='update-users'),
    path('public-servant/update/<int:id>/', updatePublicServant, name='update-public-servant'),
    path('doctor/update/<int:id>/', updateDoctor, name='update-doctor'),
    path('specialize/update/<int:id>/', updateSpecialize, name='update-specialize'),
    path('record/update/<int:id>/', updateRecord, name='update-record'),

    #delete
    path('disease-type/delete/<int:id>/', deleteDiseaseType, name='delete-disease-type'),
    path('country/delete/<int:id>/', deleteCountry, name='delete-country'),
    path('disease/delete/<int:id>/', deleteDisease, name='delete-disease'),
    path('discover/delete/<int:id>/', deleteDiscover, name='delete-discover'),
    path('users/delete/<int:id>/', deleteUsers, name='delete-users'),
    path('public-servant/delete/<int:id>/', deletePublicServant, name='delete-public-servant'),
    path('doctor/delete/<int:id>/', deleteDoctor, name='delete-doctor'),
    path('specialize/delete/<int:id>/', deleteSpecialize, name='delete-specialize'),
    path('record/delete/<int:id>/', deleteRecord, name='delete-record'),
]