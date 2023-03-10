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
from .forms import SaleRegistration
from .models import sale
from .forms import SpeciesRegistration
from .models import species
from .forms import AccreditationRegistration
from .models import Accreditation






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


def sale_data(request):
    if request.method == 'POST':
        prodvar = SaleRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = SaleRegistration()
    else:
        prodvar = SaleRegistration()
    pro = sale.objects.all()
    return render(request, 'enroll/saledata.html', {'form':prodvar, 'prod':pro})

def sale_show(request):
    pro = sale.objects.all()
    return render(request, 'enroll/saleshow.html', {'prod':pro})

def deletesale_data(request, id):
    if request.method == 'POST':
        delhat = sale.objects.get(pk=id)
        delhat.delete()
        return HttpResponseRedirect('/saleshow')
    
def updatesale_data(request, id):
    if request.method == 'POST':
        checkprod = sale.objects.get(pk=id)
        prodvar = SaleRegistration(request.POST, instance=checkprod)
        if prodvar.is_valid():
            prodvar.save()
    else:
        checkprod = sale.objects.get(pk=id)
        prodvar = SaleRegistration(instance=checkprod)
    return render(request, 'enroll/updatesaledata.html',{'form':prodvar})


def species_data(request):
    if request.method == 'POST':
        prodvar = SpeciesRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = SpeciesRegistration()
    else:
        prodvar = SpeciesRegistration()
    pro = species.objects.all()
    return render(request, 'enroll/speciesdata.html', {'form':prodvar, 'prod':pro})

def species_show(request):
    pro = species.objects.all()
    return render(request, 'enroll/speciesshow.html', {'prod':pro})


def deletespecies_data(request, id):
    if request.method == 'POST':
        delhat = species.objects.get(pk=id)
        delhat.delete()
        return HttpResponseRedirect('/speciesshow')


def updatespecies_data(request, id):
    if request.method == 'POST':
        checkprod = species.objects.get(pk=id)
        prodvar = SpeciesRegistration(request.POST, instance=checkprod)
        if prodvar.is_valid():
            prodvar.save()
    else:
        checkprod = species.objects.get(pk=id)
        prodvar = SpeciesRegistration(instance=checkprod)
    return render(request, 'enroll/updatespeciesdata.html',{'form':prodvar})



def accreditation_data(request):
    if request.method == 'POST':
        prodvar = AccreditationRegistration(request.POST)
        if prodvar.is_valid():
            prodvar.save()
            prodvar = AccreditationRegistration()
    else:
        prodvar = AccreditationRegistration()
    pro = Accreditation.objects.all()
    return render(request, 'enroll/accreditationdata.html', {'form':prodvar, 'prod':pro})

def accreditation_show(request):
    pro = Accreditation.objects.all()
    return render(request, 'enroll/accreditationshow.html', {'prod':pro})

def deleteaccreditation_data(request, id):
    if request.method == 'POST':
        delhat = Accreditation.objects.get(pk=id)
        delhat.delete()
        return HttpResponseRedirect('/accreditationshow')


def updateaccreditation_data(request, id):
    if request.method == 'POST':
        checkprod = Accreditation.objects.get(pk=id)
        prodvar = AccreditationRegistration(request.POST, instance=checkprod)
        if prodvar.is_valid():
            prodvar.save()
    else:
        checkprod = Accreditation.objects.get(pk=id)
        prodvar = AccreditationRegistration(instance=checkprod)
    return render(request, 'enroll/updateaccreditationdata.html',{'form':prodvar})

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