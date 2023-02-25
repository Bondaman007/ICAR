from django.db import models

# Create your models here.

class User(models.Model):
    accreditation_id = models.IntegerField()
    hatchery_id = models.IntegerField()
    accreditation_agency = models.CharField(max_length=100)
    term = models.CharField(max_length=70)
    year_of_accreditation = models.IntegerField()

