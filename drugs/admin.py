from django.contrib import admin
from .models import (Drugs,
DrugShipping,
DrugAvailableLocation,
DrugsInSTock)

# Register your models here.
admin.site.register(Drugs)
admin.site.register(DrugShipping)
admin.site.register(DrugAvailableLocation)
admin.site.register(DrugsInSTock)

