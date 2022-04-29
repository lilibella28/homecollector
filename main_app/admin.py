from django.contrib import admin

# Register your models here.
from .models import House, HouseSpace

admin.site.register(House)
admin.site.register(HouseSpace)
