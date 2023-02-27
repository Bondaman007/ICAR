from django.db import models

# Create your models here.

class User(models.Model):
    accreditation_id = models.IntegerField()
    hatchery_id = models.IntegerField()
    accreditation_agency = models.CharField(max_length=100)
    term = models.CharField(max_length=70)
    year_of_accreditation = models.IntegerField()


class broodstock(models.Model):
    hatchery_id = models.IntegerField()
    broodstock_type = models.CharField(max_length=70)
    name_broodstock = models.CharField(max_length=70)
    mgt_procedure_broodstock = models.IntegerField()
    no_ponds_broodstock = models.CharField(max_length=70)
    no_spawn_produce = models.CharField(max_length=70)
    species_id = models.IntegerField()
    no_fry_producing = models.IntegerField()
    no_nursery_ponds = models.CharField(max_length=70)

class cliental(models.Model):
    hatchery_id = models.IntegerField()
    clients = models.CharField(max_length=70)
    years = models.IntegerField()
    clients_id = models.IntegerField()

class cost(models.Model):
    hatchery_id = models.IntegerField()
    cost_spawn = models.CharField(max_length=70)
    cost_fry = models.CharField(max_length=70)
    cost_fingerling = models.IntegerField()
    cost_yearling = models.IntegerField()

class hatchery(models.Model):
    hatchery_id = models.IntegerField()
    hatchery_name = models.CharField(max_length=70)
    hatchery_type = models.CharField(max_length=70)
    hatchery_category = models.IntegerField()
    ownership = models.CharField(max_length=70)
    owner_name = models.CharField(max_length=70)
    hatchery_address = models.CharField(max_length=70)
    species_breeding = models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class production(models.Model):
    production_id = models.IntegerField()
    production_seed_type = models.CharField(max_length=70)
    broodstock_id = models.IntegerField()
    no_ponds_mgt = models.IntegerField()
    tech_seed_production = models.CharField(max_length=70)
    seed_production_year = models.CharField(max_length=70)
    mgt_procedures = models.IntegerField()

class species(models.Model):
    species_id = models.IntegerField()
    hatchery_id = models.IntegerField()
    species_name = models.CharField(max_length=70)


class sale(models.Model):
    hatchery_id = models.IntegerField()
    spawn_sale_year = models.CharField(max_length=70)
    fry_sale_year = models.CharField(max_length=70)
    fingerling_sale_year = models.IntegerField()
    yearling_sale_year = models.IntegerField()
    species_id = models.IntegerField()












