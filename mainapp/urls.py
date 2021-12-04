
from django.urls import path
from .views import (
    index,
    clinic_list,
    clinic_detail,
    make_request,
    delete_request,
    view_all_clinics_requested,
    view_all_accepted_clinics_requested
)

app_name = "mainapp"
urlpatterns = [
    path('',index,name="index"),
    path('clinic_list',clinic_list,name="clinic_list"),
    path('clinic_details/<id>/',clinic_detail,name="clinic_details"),
    path('make_request/',make_request,name="make_request"),
    path('delete_request/',delete_request,name="delete_request"),
    path('all_clinics_requested/',view_all_clinics_requested,name="all_clinics_requested"),
    path('view_accepted_request/',view_all_accepted_clinics_requested,name="view_accepted_request")
]

