from django.db import models
from django.contrib.auth.models import User
from datetime import date

'''
Class Venue pour cree le model de  l'evenement

'''
class Venue(models.Model):
    
    #definir les variables du form 

    titre = models.CharField('titre', max_length=120)
    owner = models.IntegerField("Venue Owner", blank=False, default=1,)
    description = models.TextField(blank=True,null=True)
    event_date = models.DateTimeField('event_date',null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=3,null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3,null=True)
    type = models.CharField('Type', choices=(
        ('sportif', 'sportif'),
        ('culturel', 'culturel'),

    ), max_length=200, null=True)
    #definir un variable pour l'utiliser de socker les images
    event_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.titre
    '''
    @property
    
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        return days_till_stripped



    @property
    def Is_Past(self):
        today = date.today()
        if self.event_date.date() < today:
            thing = "Past"
        else:
            thing = "Future"
        return thing
        '''


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
