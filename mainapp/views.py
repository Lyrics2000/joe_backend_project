from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.models import User
from drugs.models import (
    Drugs,
    DrugShipping,
    DrugAvailableLocation,
    DrugsInSTock
)
from .models import (
    OurServices,
    SlidingIMages,
    Clinics,
    ClinicTransfers
)

# Create your views here.

def index(request):
    services =  OurServices.objects.all()
    sliding =  SlidingIMages.objects.all()
    all_drugs = Drugs.objects.all()
    all_drug_shipping =  DrugShipping.objects.all()
    available_location =  DrugAvailableLocation.objects.all()
    quantity  =  DrugsInSTock.objects.filter(active = True)
    clinic =  Clinics.objects.all()

    context = {
        'services' :  services,
        'sliding' :  sliding,
        'drugs' :  all_drugs,
        'shipping' :  all_drug_shipping,
        'location' :  available_location,
        'quantity' :  quantity,
        'clinics' :  clinic
     }


    return render(request,'index.html',context)


def clinic_list(request):

    clinics =  Clinics.objects.all()
    context = {
        'clinics' : clinics
    }
    return render(request,'clinic_list.html',context)


# @login_required(login_url="account:sign_in")
def clinic_detail(request,id):
    clinicc =  Clinics.objects.get(id = id)
    clinic_transfer =  ClinicTransfers.objects.all()
    context = {
        'clinic' :  clinicc,
        'clinic_transfers' :  clinic_transfer
    }
    return render(request,'clinic_details.html',context)

@login_required(login_url="account:sign_in")
def make_request(request):
    if request.method == "POST":
        user_id =  request.user.id
        user_obj =  User.objects.get(id =  user_id)
        clinic_id =  request.POST.get("clinic_id")
        clinic_obj =  Clinics.objects.get(id =  clinic_id)
        ClinicTransfers.objects.create(
            clinic =  clinic_obj,
            user_id = user_obj,
            transfer_request =  True
        )
      
        return redirect("/")


@login_required(login_url="account:sign_in")
def delete_request(request):
    if request.method == "POST":
        user_id =  request.user.id
        user_obj =  User.objects.get(id =  user_id)
        clinic_id =  request.POST.get("clinic_id")
        clinic_obj = Clinics.objects.get(id =  clinic_id)
        ClinicTransfers.objects.get(
            clinic =  clinic_obj
        ).delete()
        
     
        return redirect("/")

@login_required(login_url="account:sign_in")
def view_all_clinics_requested(request):
    user_id = request.user.id
    user_obj =  User.objects.get(id =  user_id)
    all_transfer  =  ClinicTransfers.objects.filter(user_id = user_obj)
    context = {
        'all_transfer': all_transfer
    }
    return render(request,'all_clinics_requested.html',context)


@login_required(login_url="account:sign_in")
def view_all_accepted_clinics_requested(request):
    user_id = request.user.id
    user_obj =  User.objects.get(id =  user_id)
    all_transfer  =  ClinicTransfers.objects.filter(user_id = user_obj)
    context = {
        'all_transfer': all_transfer
    }
    return render(request,'view_accepted_request.html',context)

