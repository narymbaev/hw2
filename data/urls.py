from django.urls import path
from .views import diseaseType, country, disease, discover, users, publicServant, doctor, specialize, record

urlpatterns = [
    path('disease-type/', diseaseType, name='disease-type'),
    path('country/', country, name='country'),
    path('disease/', disease, name='disease'),
    path('discover/', discover, name='discover'),
    path('users/', users, name='users'),
    path('public-servant/', publicServant, name='public-servant'),
    path('doctor/', doctor, name='doctor'),
    path('specialize/', specialize, name='specialize'),
    path('record/', record, name='record'),
]