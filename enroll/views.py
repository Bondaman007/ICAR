from django.shortcuts import render, HttpResponseRedirect
from icarinternship import settings
from .forms import StudentRegistration
from .models import User

# Create your views here.

def datapage(request):
    return render(request,'enroll/datapage.html')

# This Function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def insert_sale(request):
    return render(request, 'enroll/sale.html')

def insert_hatchery(request):
    return render(request, 'enroll/hatchery.html')

def insert_production(request):
    return render(request, 'enroll/production.html')

def insert_broodstock(request):
    return render(request, 'enroll/broodstock.html')

def insert_cliental(request):
    return render(request, 'enroll/cliental.html')

def insert_species(request):
    return render(request, 'enroll/species.html')

def insert_cost(request):
    return render(request, 'enroll/cost.html')