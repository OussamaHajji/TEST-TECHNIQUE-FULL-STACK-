from django import forms
from django.forms import ModelForm
from .models import Venue

'''
Class VenueForm definir le form du l'evenement
'''
# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        #definir les filed du form 
        fields = ('titre', 'type', 'event_date',
                  'description', 'latitude','longitude','event_image')
        
         #definir les labels du form 

        labels = {
            'titre': '',
            'type': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            'latitude': '',
	        'longitude': '',
            'event_image': '',
        }

        #definir les widgets du form 

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'longitude'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Date'}),
            'type': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Type'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }
