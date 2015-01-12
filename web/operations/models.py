from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
# 
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=15,blank=True)
    fax = models.CharField(max_length=30,blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return ' '.join([self.first_name,self.last_name])

    class Meta:
        abstract = True

class Driver(Person):
    on_leave = models.BooleanField(default=False)
    history = HistoricalRecords()

class Truck(models.Model):
    license_plate = models.CharField(max_length=10)
    assigned_driver = models.ForeignKey('Driver',null=True,blank=True)
    assigned_customer = models.ForeignKey('Customer',null=True,blank=True)
    in_garage = models.BooleanField(default=False)
    history = HistoricalRecords()


    def __str__(self):
        return self.license_plate    


class Contact(Person):
    #pass
    history = HistoricalRecords()

class Company(models.Model):
    name = models.CharField(max_length=80)
    address = models.TextField(blank=True)
    contacts = models.ManyToManyField(Contact,blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Customer(Company):
    history = HistoricalRecords()
    #pass

class Location(models.Model):
    name = models.CharField(max_length=10)
    history = HistoricalRecords()

    def __str__(self):
        return self.name