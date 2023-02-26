from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['accreditation_id', 'hatchery_id', 'accreditation_agency', 'term', 'year_of_accreditation' ]