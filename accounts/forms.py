from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import Report


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['location','Incident_Department','Incident_Location','initial_severity','Suspected_Cause','Immediate_Action_taken','Sub_Incidents_types']
        widget = {
            'Incident_Department' : forms.Textarea(attrs={'class':'form.control','rows':4, 'cols':4}),
            'Incident_Location' :   forms.Textarea(attrs={'class':'form.control'}),
            'Suspected_Cause' :     forms.Textarea(attrs={'class':'form.control'}),
            'Immediate_Action_taken': forms.Textarea(attrs={'class':'form.control'}),
            
            }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2']
