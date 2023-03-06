from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from enroll import views

urlpatterns = [
    path('datapage',views.datapage, name="datapage"),
    #path('occur', views.insert_occur, name="occur"),
    path('insert_sale', views.insert_sale, name="sale"),
    path('insert_hatchery', views.insert_hatchery, name="hatchery"),
    path('insert_production', views.insert_production, name="production"),
    path('insert_broodstock', views.insert_broodstock, name="broodstock"),
    path('insert_cliental', views.insert_cliental, name="cliental"),
    path('insert_species', views.insert_species, name="species"),
    path('insert_cost', views.insert_cost, name="cost"),



    path('addandshow',views.add_show, name="addandshow"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),

    path('brood',views.brood_show, name="broodshow"),
    path('brooddata',views.brood_data, name="brooddata"),
    path('<int:id>/', views.updatebrood_data, name="updatebrooddata"),
    path('delete/<int:id>/', views.deletebrood_data, name="deletebrooddata"),

    path('clientaldata',views.cliental_data, name="clientaldata"), 
    path('/<int:id>/', views.updatecliental_data, name="updateclientaldata"),
    path('/delete/<int:id>/', views.deletecliental_data, name="deleteclientaldata"),
    path('clientalshow',views.cliental_show, name="clientalshow"),


    path('costdata',views.cost_data, name="costdata"), 
    path('costshow',views.cost_show, name="costshow"),
    path('/<int:id>/', views.updatecost_data, name="updatecostdata"),
    path('/delete/<int:id>/', views.deletecost_data, name="deletecostdata"),


    path('productiondata',views.production_data, name="productiondata"), 
    path('productionshow',views.production_show, name="productionshow"),
    path('/<int:id>/', views.updateproduction_data, name="updateproductiondata"),


    path('hatcherydata',views.hatchery_data, name="hatcherydata"),
    path('hatcheryshow',views.hatchery_show, name="hatcheryshow"),
    path('hatcheryshow/delete/<int:id>/', views.deletehatchery_data, name="deletehatcherydata"),
    path('hatcheryshow/<int:id>/', views.updatehatchery_data, name="updatehatcherydata"),


]