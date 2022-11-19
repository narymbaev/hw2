from django.db import models

# Create your models here.
class DiseaseType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    class Meta:
        db_table = 'disease_type'
        verbose_name_plural = 'Disease Type'
    
    def __str__(self) -> str:
        return self.description

class Country(models.Model):
    cname = models.CharField(max_length=50, blank=False, null=False)
    population = models.IntegerField(blank=False, null=False)
    class Meta:
        db_table = "country"
        verbose_name_plural = "country"
    
    def __str__(self) -> str:
        return self.cname

class Disease(models.Model):
    disease_code = models.CharField(max_length=50, blank=False, null=False)
    pathogen = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=140)
    disease_type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    class Meta:
        db_table = 'disease'
        verbose_name_plural = 'disease'
    
    def __str__(self) -> str:
        return self.disease_code


class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False, null=False)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE, blank=False, null=False)
    first_enc = models.DateField()
    class Meta:
        db_table = 'discover'
    
    def __str__(self) -> str:
        return self.first_enc.strftime('%d-%m-%Y')

class Users(models.Model):
    email = models.CharField(max_length=60, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    surname = models.CharField(max_length=40, blank=False, null=False)
    salary = models.IntegerField(default=0, blank=False, null=False)
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False, null=False)
    class Meta:
        db_table = 'users'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.email

class PublicServant(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, null=False)
    department = models.CharField(max_length=50, blank=False, null=False)
    class Meta:
        db_table = 'public_servant'

    def __str__(self) -> str:
        return self.email.__str__()

class Doctor(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, null=False)
    degree = models.CharField(max_length=20)
    class Meta:
        db_table = 'doctor'
    
    def __str__(self) -> str:
        return self.email.__str__()

class Specialize(models.Model):
    disease_type = models.ForeignKey(DiseaseType, on_delete=models.CASCADE, blank=False, null=False)
    email = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=False, null=False)
    class Meta:
        db_table = 'specialize'

    def __str__(self) -> str:
        return self.email.__str__() + " --> " + self.disease_type.__str__()

class Record(models.Model):
    email = models.ForeignKey(PublicServant, on_delete=models.CASCADE, blank=False, null=False)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False, null=False)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE, blank=False, null=False)
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()
    class Meta:
        db_table = 'record'

    def __str__(self) -> str:
        return self.email.__str__() + " --> " + self.disease_code.__str__()
