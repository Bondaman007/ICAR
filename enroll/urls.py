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
    path('brood',views.brood_show, name="broodshow"),
    path('brooddata',views.brood_data, name="brooddata"),
    path('<int:id>/', views.updatebrood_data, name="updatebrooddata"),
    path('delete/<int:id>/', views.deletebrood_data, name="deletebrooddata"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),

    path('clientaldata',views.cliental_data, name="clientaldata"), 

    path('<int:id>/', views.updatecliental_data, name="updateclientaldata"),

    path('delete/<int:id>/', views.deletecliental_data, name="deleteclientaldata"),

    path('clientalshow',views.cliental_show, name="clientalshow"),


    
]