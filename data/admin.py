from django.contrib import admin
from .models import Country, DiseaseType, Disease, Discover, Doctor, Users, Specialize, PublicServant, Record
# Register your models here.
admin.site.register(DiseaseType)
admin.site.register(Country)
admin.site.register(Disease)
admin.site.register(Discover)
admin.site.register(Users)
admin.site.register(Doctor)
admin.site.register(Specialize)
admin.site.register(PublicServant)
admin.site.register(Record)