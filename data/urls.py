from django.urls import path
from .views import *

urlpatterns = [
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
    path('disease-type/create/', diseaseType, name='disease-type'),
    path('country/create/', country, name='country'),
    path('disease/create/', disease, name='disease'),
    path('discover/create/', discover, name='discover'),
    path('users/create/', users, name='users'),
    path('public-servant/create/', publicServant, name='public-servant'),
    path('doctor/create/', doctor, name='doctor'),
    path('specialize/create/', specialize, name='specialize'),
    path('record/create/', record, name='record'),

    #update
    path('disease-type/update/<int:id>/', diseaseType, name='disease-type'),
    path('country/update/<cname>/', country, name='country'),
    path('disease/update/<disease_code>/', disease, name='disease'),
    path('discover/update/<int:id>/', discover, name='discover'),
    path('users/update/<email>/', deleteUsers, name='delete-users'),
    path('public-servant/update/<email_id>/', publicServant, name='public-servant'),
    path('doctor/update/<email_id>/', doctor, name='doctor'),
    path('specialize/update/<int:id>/', specialize, name='specialize'),
    path('record/update/<int:id>/', record, name='record'),

    #delete
    path('disease-type/delete/<int:id>/', diseaseType, name='disease-type'),
    path('country/delete/<cname>/', country, name='country'),
    path('disease/delete/<disease_code>/', disease, name='disease'),
    path('discover/delete/<int:id>/', discover, name='discover'),
    path('users/delete/<email>/', deleteUsers, name='delete-users'),
    path('public-servant/delete/<email_id>/', publicServant, name='public-servant'),
    path('doctor/delete/<email_id>/', doctor, name='doctor'),
    path('specialize/delete/<int:id>/', specialize, name='specialize'),
    path('record/delete/<int:id>/', record, name='record'),
]