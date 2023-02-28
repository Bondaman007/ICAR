from django.core import validators
from django import forms
from .models import User
from .models import broodstock

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['accreditation_id', 'hatchery_id', 'accreditation_agency', 'term', 'year_of_accreditation']
        fields = "__all__"

class BroodstockRegistration(forms.ModelForm):
    class Meta:
        model = broodstock
        #fields = ['hatchery_id','broodstock_type','name_broodstock','mgt_procedure_broodstock','no_ponds_broodstock','no_spawn_produce','species_id','no_fry_producing','no_nursery_ponds']
        fields = "__all__"