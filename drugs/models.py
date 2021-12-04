from django.db import models
from django.db.models.signals import post_save
from account.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Notifications(BaseModel):
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    message =  models.TextField()

    def __str__(self):
        return str(self.user_id)
# Create your models here.
class Drugs(models.Model):
    drug_type =  models.CharField(max_length=255)
    drug_name =  models.CharField(max_length=255)

    def __str__(self):
        return self.drug_name


class DrugShipping(models.Model):
    drug_id =  models.ForeignKey(Drugs,on_delete=models.CASCADE)
    shipping_date =  models.DateTimeField()
    expected_arrival_time =  models.DateTimeField()


    def __str__(self):
        return str(self.drug_id)

class DrugAvailableLocation(models.Model):
    drug_id =  models.ForeignKey(Drugs,on_delete=models.CASCADE)
    location_name =  models.CharField(max_length=255)
   

    def __str__(self):
        return str(self.drug_id)


class DrugsInSTock(models.Model):
    drug_id =  models.ForeignKey(Drugs,on_delete=models.CASCADE)
    initial_qty =  models.IntegerField()
    final_qty =  models.IntegerField(blank=True,null=True)
    active =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.drug_id)


def send_drug_email(sender,instance,created,**kwargs):
    if created:
        users =  User.objects.all()
        if users:
            for m in users:
                Notifications.objects.create(
                    user_id = m,
                    message = f"A new Drug {instance.drug_name} of type {instance.drug_type} is available"
                )
                try:
                    
                    email_subject = 'New Drug available'
                    message = render_to_string('send_email.html', {
                    'user': m.username,
                    'drug' : instance.drug_name,
                    'drug_type' :  instance.drug_type
                    })
                    to_email = m.email
                    email = EmailMessage(email_subject, message, to=[to_email])
                    email.send()

                except:
                    print("user do not exist")

post_save.connect(send_drug_email,sender =Drugs )

