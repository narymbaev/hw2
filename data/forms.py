from django.forms import ModelForm
from .models import *

class DiseaseTypeForm(ModelForm):
    class Meta:
        model = DiseaseType
        fields = '__all__'

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = '__all__'

class DiscoverForm(ModelForm):
    class Meta:
        model = Discover
        fields = '__all__'

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class PublicServantForm(ModelForm):
    class Meta:
        model = PublicServant
        fields = '__all__'

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class SpecializeForm(ModelForm):
    class Meta:
        model = Specialize
        fields = '__all__'

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = '__all__'