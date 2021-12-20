from django import forms
from django.forms import ModelForm 
from .models import DeiselReport, Engineer, Site, SiteReport

# existing
class SiteForm(ModelForm):
    class Meta:
        model = Site
        fields = ("fields meant for the Site model ONLY")

class NewRequestForm(ModelForm):
    
    class Meta:
        models = Site
        fields = ("fields meant for New Request + additional fields from the Site model")
    
     
     
    
     


