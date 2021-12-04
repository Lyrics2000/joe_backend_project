from django.contrib import admin

from .models import (
    OurServices,
    SlidingIMages,
    Clinics,
    ClinicTransfers,
    AllBroadcast
)

# Register your models here.

admin.site.register(OurServices)
admin.site.register(SlidingIMages)
admin.site.register(Clinics)
admin.site.register(ClinicTransfers)
admin.site.register(AllBroadcast)
