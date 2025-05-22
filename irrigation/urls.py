"""irrigation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from irrigationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('seregistration', views.seregistration, name='seregistration'),
    path('jeregistration', views.jeregistration, name='jeregistration'),
    path('overseerregistration', views.overseerregistration,
         name='overseerregistration'),
    path('contractorregistration', views.contractorregistration,
         name='contractorregistration'),
    path('adminse', views.adminse, name='adminse'),
    path('adminje', views.adminje, name='adminje'),
    path('adminoverseer', views.adminoverseer, name='adminoverseer'),
    path('admincontractor', views.admincontractor, name='admincontractor'),
    path('adminapproveuser', views.adminapproveuser, name='adminapproveuser'),
    path('sehome', views.sehome, name='sehome'),
    path('seProfile', views.seProfile, name='seProfile'),
    path('sejengineer', views.sejengineer, name='sejengineer'),
    path('seoverseer', views.seoverseer, name='seoverseer'),
    path('secontractor', views.secontractor, name='secontractor'),
    path('complaint', views.complaint, name='complaint'),
    path('admincomplaint', views.admincomplaint, name='admincomplaint'),
    path('adminAssignSe', views.adminAssignSe, name='adminAssignSe'),
    path('secomplaint', views.secomplaint, name='secomplaint'),
    path('seproject', views.seproject, name='seproject'),
    path('seselectje', views.seselectje, name='seselectje'),
    path('seje', views.seje, name='seje'),
    path('seselectoverseer', views.seselectoverseer, name='seselectoverseer'),
    path('seos', views.seos, name='seos'),
    path('seprojectforestimation', views.seprojectforestimation,
         name='seprojectforestimation'),
    path('jehome', views.jehome, name='jehome'),
    path('jeProfile', views.jeProfile, name='jeProfile'),
    path('jeprojectforestimation', views.jeprojectforestimation,
         name='jeprojectforestimation'),
    path('jecostestimation', views.jecostestimation, name='jecostestimation'),
    path('seprojectstatus', views.seprojectstatus, name='seprojectstatus'),
    path('seprojectestimation', views.seprojectestimation,
         name='seprojectestimation'),
    path('adminproject', views.adminproject, name='adminproject'),
    path('adminprojectestimation', views.adminprojectestimation,
         name='adminprojectestimation'),
    path('adminprojectupdate', views.adminprojectupdate, name='adminprojectupdate'),
    path('adminapprovedproject', views.adminapprovedproject,
         name='adminapprovedproject'),
    path('seapprovedproject', views.seapprovedproject, name='seapprovedproject'),
    path('overseerhome', views.overseerhome, name='overseerhome'),
    path('osProfile', views.osProfile, name='osProfile'),
    path('osprojectforsite', views.osprojectforsite, name='osprojectforsite'),
    path('ossite', views.ossite, name='ossite'),
    path('osapprovedproject', views.osapprovedproject, name='osapprovedproject'),
    path('osfundrequest', views.osfundrequest, name='osfundrequest'),
    path('jefundrequest', views.jefundrequest, name='jefundrequest'),
    path('jefundrequestupdate', views.jefundrequestupdate,
         name='jefundrequestupdate'),
    path('sefundrequest', views.sefundrequest, name='sefundrequest'),
    path('sefundrequestupdate', views.sefundrequestupdate,
         name='sefundrequestupdate'),
    path('osfundrequeststatus', views.osfundrequeststatus,
         name='osfundrequeststatus'),
    path('osComplaint', views.osComplaint, name='osComplaint'),
    path('osConComp', views.osConComp, name='osConComp'),
    path('contractorhome', views.contractorhome, name='contractorhome'),
    path('coProfile', views.coProfile, name='coProfile'),
    path('contractorproject', views.contractorproject, name='contractorproject'),
    path('contractorquotation', views.contractorquotation,
         name='contractorquotation'),
    path('contractorquots', views.contractorquots, name='contractorquots'),
    path('sequotations', views.sequotations, name='sequotations'),
    path('sequotationupdate', views.sequotationupdate, name='sequotationupdate'),



     path('farmerregistration', views.farmerregistration, name='farmerregistration'),
     path('officerregistration', views.officerregistration, name='officerregistration'),
     path('adminfarmer', views.adminfarmer, name='adminfarmer'),
     path('adminofficer', views.adminofficer, name='adminofficer'),
     path('adminviewfarmercomplaint', views.adminviewfarmercomplaint, name='adminviewfarmercomplaint'),
     path('farmerhome', views.farmerhome, name='farmerhome'),
     path('farmerComplaint', views.farmerComplaint, name='farmerComplaint'),
     path('farmerViewComplaint', views.farmerViewComplaint, name='farmerViewComplaint'),
     path('farmerProfile', views.farmerProfile, name='farmerProfile'),
     path('officerhome', views.officerhome, name='officerhome'),
     path('officerComplaint', views.officerComplaint, name='officerComplaint'),
     path('officerUpdateComplaintStatus', views.officerUpdateComplaintStatus, name='officerUpdateComplaintStatus'),
     path('officerComplaintRespond', views.officerComplaintRespond, name='officerComplaintRespond'),
     path('officerComplaintHistory', views.officerComplaintHistory, name='officerComplaintHistory'),
     path('officerProfile', views.officerProfile, name='officerProfile'),
     path('about', views.about, name='about'),
]
