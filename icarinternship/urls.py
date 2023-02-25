"""icarinternship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cliental.views import clientalaction
#from accreditation.views import accreditationaction
from broodstock.views import broodstockaction
from cost.views import costaction
from mainpage.views import mainpageaction
from loginpage.views import loginpageaction
from signuppage.views import signupaction
from adminloginpage.views import adminloginaction
from django.conf import settings
from django.conf.urls.static import static
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliental/',clientalaction),
    path('broodstock/',broodstockaction),
    path('cost/',costaction),
    path('mainpage/',mainpageaction),
    path('loginpage/',loginpageaction),
    path('signuppage/',signupaction),
    path('adminloginpage/',adminloginaction),
    path('', include('authentication.urls')),
    path('', include('enroll.urls')),
    path('',views.add_show, name="addandshow"),
    #path('accreditation/', views.insert_accre, name="insert_accre")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 