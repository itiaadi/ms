from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Report(models.Model):

    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    LOCATION = (
        ('Corporate Headoffice' , 'Corporate Headoffice'),
        ('Operation Department' , 'Operation Department'),
        ('Work Station', 'Work Station'),
        ('Marketing Division' , 'Marketing Division'),
   
        )
    location = models.CharField(max_length=200, null=True,choices=LOCATION)
    Incident_Department = models.TextField(null=True)
    Incident_Location = models.TextField(null=True)
    INITIAL_SEVERITY = (
        ('Mild' , 'Mild'),
        ('Moderate' , 'Moderate'),
        ('Severe', 'Severe'),
        ('Fatal' , 'Fatal'),
   
        )
    initial_severity = models.CharField(max_length=200,null=True,choices=INITIAL_SEVERITY)
    Suspected_Cause = models.TextField(null=True)
    Immediate_Action_taken = models.TextField(null=True)
    SUB_INCIDENT_TYPES = (
        ('Environmental Incident' , 'Environmental Incident'),
        ('Injuiry/Illness' , 'Injuiry/Illness'),
        ('Property Damage', 'Property Damage'),
        ('Vehicle' , 'Vehicle'),
   
        )
    Sub_Incidents_types = models.CharField(max_length=200, null=True,choices=SUB_INCIDENT_TYPES)

  