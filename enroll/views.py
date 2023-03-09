from django.shortcuts import render, HttpResponseRedirect
from icarinternship import settings
from .forms import StudentRegistration
from .forms import BroodstockRegistration
from .models import User
from .models import broodstock
from .models import cliental
from .forms import ClientalRegistration
from .forms import CostRegistration
from .models import cost
from .forms import ProductionRegistration
from .models import production
from .forms import HatcheryRegistration
from .models import hatchery




# Create your views here.

def datapage(request):
    return render(request,'enroll/datapage.html')


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

# This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow')
    

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



def brood_data(request):
    if request.method == 'POST':
        bs = BroodstockRegistration(request.POST)
        if bs.is_valid():
            bs.save()
            bs = BroodstockRegistration()
    else:
        bs = BroodstockRegistration()
    btud = broodstock.objects.all()
    return render(request, 'enroll/brooddata.html', {'form':bs, 'btu':btud})


def brood_show(request):
    if request.method == 'POST':
        bs = BroodstockRegistration(request.POST)
        if bs.is_valid():
            bs.save()
            bs = BroodstockRegistration()
    else:
        bs = BroodstockRegistration()
    btud = broodstock.objects.all()
    return render(request, 'enroll/broodshow.html', {'form':bs, 'btu':btud}) 

# This Function will Delete Brood Data
def deletebrood_data(request,id):
    if request.method == 'POST':
        bi = broodstock.objects.get(pk=id)
        bi.delete()
        return HttpResponseRedirect('/')

# This Function will Update/Edit

def updatebrood_data(request, id):
    if request.method == 'POST':
        bi = broodstock.objects.get(pk=id)
        bs = BroodstockRegistration(request.POST, instance=bi)
        if bs.is_valid():
            bs.save()
    else:
        bi = broodstock.objects.get(pk=id)
        bs = BroodstockRegistration(instance=bi)
    return render(request, 'enroll/updatebrood.html',{'form':bs})



def cliental_data(request):
    if request.method == 'POST':
        clientvar = ClientalRegistration(request.POST)
        if clientvar.is_valid():
            clientvar.save()
            clientvar = ClientalRegistration()
    else:
        clientvar = ClientalRegistration()
    client = cliental.objects.all()
    return render(request, 'enroll/clientaldata.html', {'form':clientvar, 'clie':client})

def cliental_show(request):
    if request.method == 'POST':
        clientvar = ClientalRegistration(request.POST)
        if clientvar.is_valid():
            clientvar.save()
            clientvar = ClientalRegistration()
    else:
        clientvar = ClientalRegistration()
    client = cliental.objects.all()
    return render(request, 'enroll/clientalshow.html', {'form':clientvar, 'clie':client}) 


def updatecliental_data(request, id):
    if request.method == 'POST':
        clinst = cliental.objects.get(pk=id)
        clientvar = ClientalRegistration(request.POST, instance=clinst)
        if clientvar.is_valid():
            clientvar.save()
    else:
        clinst = cliental.objects.get(pk=id)
        clientvar = ClientalRegistration(instance=clinst)
    return render(request, 'enroll/updatecliental.html', {'form':clientvar})


def deletecliental_data(request,id):
    if request.method == 'POST':
        clinst = cliental.objects.get(pk=id)
        clinst.delete()
        return HttpResponseRedirect('/')
    



def cost_data(request):
    if request.method == 'POST':
        costvar = CostRegistration(request.POST)
        if costvar.is_valid():
            costvar.save()
            costvar = CostRegistration()
    else:
        costvar = CostRegistration()
    cos = cost.objects.all()
    return render(request, 'enroll/costdata.html', {'form':costvar, 'coss':cos})

def cost_show(request):
    if request.method == 'POST':
        costvar = CostRegistration(request.POST)
        if costvar.is_valid():
            costvar.save()
            costvar = CostRegistration()
    else:
        costvar = CostRegistration()
    cos = cost.objects.all()
    return render(request, 'enroll/costshow.html', {'form':costvar, 'coss':cos})

def updatecost_data(request, id):
    if request.method == 'POST':
        check = cost.objects.get(pk=id)
        costvar = CostRegistration(request.POST, instance=check)
        if costvar.is_valid():
            costvar.save()
    else:
        check = cost.objects.get(pk=id)
        costvar = CostRegistration(instance=check)
    return render(request, 'enroll/updatecostdata.html',{'form':costvar})

def deletecost_data(request,id):
    if request.method == 'POST':
        check = cost.objects.get(pk=id)
        check.delete()
        return HttpResponseRedirect('/')


def production_data(request):
    if request.method == 'POST':
        prodvar = ProductionRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = ProductionRegistration()
    else:
        prodvar = ProductionRegistration()
    pro = production.objects.all()
    return render(request, 'enroll/productiondata.html', {'form':prodvar, 'prod':pro})

def production_show(request):
    if request.method == 'POST':
        prodvar = ProductionRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = ProductionRegistration()
    else:
        prodvar = ProductionRegistration()
    pro = production.objects.all()
    return render(request, 'enroll/productionshow.html', {'form':prodvar, 'prod':pro})

def updateproduction_data(request, id):
    if request.method == 'POST':
        checkprod = production.objects.get(pk=id)
        prodvar = ProductionRegistration(request.POST, instance=checkprod)
        if prodvar.is_valid():
            prodvar.save()
    else:
        checkprod = production.objects.get(pk=id)
        prodvar = ProductionRegistration(instance=checkprod)
    return render(request, 'enroll/updateproductiondata.html',{'form':prodvar})


def deleteproduction_data(request,id):
    if request.method == 'POST':
        checkprod = production.objects.get(pk=id)
        checkprod.delete()
        return HttpResponseRedirect('/productionshow')



def hatchery_data(request):
    if request.method == 'POST':
        prodvar = HatcheryRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = HatcheryRegistration()
    else:
        prodvar = HatcheryRegistration()
    pro = hatchery.objects.all()
    return render(request, 'enroll/hatcherydata.html', {'form':prodvar, 'prod':pro})

def hatchery_show(request):
    pro = hatchery.objects.all()
    return render(request, 'enroll/hatcheryshow.html', {'prod':pro})

def deletehatchery_data(request, id):
    if request.method == 'POST':
        delhat = hatchery.objects.get(pk=id)
        delhat.delete()
        return HttpResponseRedirect('/hatcheryshow')


def updatehatchery_data(request, id):
    if request.method == 'POST':
        checkprod = hatchery.objects.get(pk=id)
        prodvar = HatcheryRegistration(request.POST, instance=checkprod)
        if prodvar.is_valid():
            prodvar.save()
    else:
        checkprod = hatchery.objects.get(pk=id)
        prodvar = HatcheryRegistration(instance=checkprod)
    return render(request, 'enroll/updatehatcherydata.html',{'form':prodvar})



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