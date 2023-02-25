from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','accreditation_id','hatchery_id','accreditation_agency','term','year_of_accreditation')

