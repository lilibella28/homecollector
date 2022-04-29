from django.db import models
# from location_field.models.plain import PlainLocationField
from django.urls import reverse

# Create your models here.
class Feature(models.Model):
     name = models.CharField(max_length=50)
     feauture_type = models.CharField(max_length=50)

     def __str__(self):
          return self.name
     
     def get_absolute_url(self):
          return reverse('features_detail', kwargs={'pk': self.id})

     

class House(models.Model):
     price = models.FloatField()
     location = models.CharField(max_length=100)
     property_type = models.CharField(max_length=100)
     year_build = models.IntegerField()
     special_note = models.CharField(max_length=300)
     features = models.ManyToManyField(Feature) #create M:M relationship between House and feature

     # def __str__(self):
     #      return self.price

     def get_absolute_url(self):
          return reverse('detail', kwargs={'house_id': self.id})

SPACES = (
     ('B', 'Bedroom'),
     ('T', 'BATHROOM'),
     ('O', 'Office')
)


class HouseSpace(models.Model):
     room_meausure = models.IntegerField()
     room_type = models.CharField(max_length=1,
     choices=SPACES,
     default=SPACES[0][0]
     )
     house = models.ForeignKey(House, on_delete=models.CASCADE)

     def __str__(self):
          return f" {self.get_room_type_display()} on {self.room_meausure}"

     class Meta: 
          ordering = ['-room_meausure']
