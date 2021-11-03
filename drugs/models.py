from django.db import models

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
    latitude =  models.CharField(max_length=255)
    longitude =  models.CharField(max_length=255)

    def __str__(self):
        return str(self.drug_id)


class DrugsInSTock(models.Model):
    drug_id =  models.ForeignKey(Drugs,on_delete=models.CASCADE)
    initial_qty =  models.IntegerField()
    final_qty =  models.IntegerField(blank=True,null=True)
    active =  models.BooleanField(default=False)

    def __str__(self):
        return str(self.drug_id)

