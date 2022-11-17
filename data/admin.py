from django.contrib import admin
from .models import Country, DiseaseType, Disease, Depart, Student
# Register your models here.
admin.site.register(DiseaseType)
admin.site.register(Country)
admin.site.register(Disease)