from django.forms import ModelForm
from .models import HouseSpace 

class HouseSpaceForm(ModelForm):
    class Meta:
        model = HouseSpace 
        fields = ['room_meausure', 'room_type']