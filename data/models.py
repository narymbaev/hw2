from django.db import models

# Create your models here.
class DiseaseType(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    description = models.CharField(max_length=140, blank=True, null=True)
    class Meta:
        db_table = 'disease_type'
        verbose_name_plural = 'Disease Type'
    
    def __str__(self) -> str:
        return self.description

class Country(models.Model):
    cname = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    population = models.BigIntegerField(blank=False, null=False)
    class Meta:
        db_table = "country"
        verbose_name_plural = "country"
    
    def __str__(self) -> str:
        return self.cname

class Disease(models.Model):
    disease_code = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    pathogen = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    class Meta:
        db_table = 'disease'
        verbose_name_plural = 'disease'
    
    def __str__(self) -> str:
        return self.disease_code


class Depart(models.Model):
    zxc = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=140, primary_key=True)
    qwe = models.ForeignKey(Depart, on_delete=models.CASCADE)
