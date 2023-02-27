from django.contrib import admin
from .models import User
from .models import broodstock
from .models import cliental
from .models import cost
from .models import hatchery
from .models import production
from .models import species
from .models import sale






# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','accreditation_id','hatchery_id','accreditation_agency','term','year_of_accreditation')

@admin.register(broodstock)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hatchery_id','broodstock_type','name_broodstock','mgt_procedure_broodstock','no_ponds_broodstock','no_spawn_produce','species_id','no_fry_producing','no_nursery_ponds')

@admin.register(cliental)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hatchery_id','clients','years','clients_id')

@admin.register(cost)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hatchery_id','cost_spawn','cost_fry','cost_fingerling','cost_yearling')


@admin.register(hatchery)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hatchery_id','hatchery_name','hatchery_name','hatchery_type','hatchery_category','ownership','owner_name','hatchery_address','species_breeding','city')


@admin.register(production)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','production_id','production_seed_type','broodstock_id','no_ponds_mgt','tech_seed_production','seed_production_year','mgt_procedures')

@admin.register(species)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','species_id','hatchery_id','species_name')

@admin.register(sale)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','hatchery_id','spawn_sale_year','fry_sale_year','fingerling_sale_year','yearling_sale_year','species_id')