from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signuppage', views.signuppage, name="signuppage"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    #path('datapage',views.datapage, name="datapage"),
    #path('insert_accre', views.insert_accre, name="accreditation"),
]