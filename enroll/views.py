from django.shortcuts import render, HttpResponseRedirect
from icarinternship import settings
from .forms import StudentRegistration
from .forms import BroodstockRegistration
from .models import User
from .models import broodstock


# Create your views here.

def datapage(request):
    return render(request,'enroll/datapage.html')

def brood_data(request):
    return render(request,'enroll/brooddata.html')

# This Function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            ai = fm.cleaned_data['accreditation_id']
            hi = fm.cleaned_data['hatchery_id']
            aa = fm.cleaned_data['accreditation_agency']
            tr = fm.cleaned_data['term']
            ya = fm.cleaned_data['year_of_accreditation']
            reg = User(accreditation_id=ai, hatchery_id=hi, accreditation_agency=aa, term=tr, year_of_accreditation=ya)
            reg.save()            
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

def brood_show(request):
    if request.method == 'POST':
        bs = BroodstockRegistration(request.POST)
        if bs.is_valid():
            bs.save()
            bs = BroodstockRegistration()
    else:
        bs = BroodstockRegistration()
    brood = broodstock.objects.all()
    return render(request, 'enroll/brood.html', {'form':bs, 'btu':brood})

        

        










# This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

# This Function will Update/Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html',{'form':fm})


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