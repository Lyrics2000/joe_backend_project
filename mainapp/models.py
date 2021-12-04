from django.db import models
import os
import random
from account.models import User
from drugs.models import BaseModel
from django.shortcuts import reverse


# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "restaurants/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )

class OurServices(models.Model):
    services =  models.CharField(max_length=255)
    

    def __str__(self):
        return self.services


class SlidingIMages(models.Model):
    header1 =  models.CharField(max_length=255)
    header2 =  models.CharField(max_length=255)
    body =  models.TextField()
    image = models.ImageField(upload_to=upload_image_path)

    def __str__(self):
        return self.header1

class Clinics(BaseModel):
    name =  models.CharField(max_length=255)
    clinic_description = models.TextField(blank=True,null = True)
    image =  models.ImageField(upload_to = upload_image_path)
    locatione_name =  models.CharField(max_length=255)


    def __str__(self):
        return str(self.name)

    
    def get_absolute_url_clinic(self):
        return reverse("mainapp:clinic_details", kwargs={
            'id': self.id
        })


class ClinicTransfers(BaseModel):
    clinic =  models.ForeignKey(Clinics,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    transfer_request =  models.BooleanField(default=False)
    accept_transfer_request =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)


class AllBroadcast(BaseModel):
    message =  models.TextField()

    def __str__(self):
        return self.message



