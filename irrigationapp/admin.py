from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Sengineer)
admin.site.register(Jengineer)
admin.site.register(Overseer)
admin.site.register(Contractor)
admin.site.register(Project)
admin.site.register(Estimation)
admin.site.register(Site)
admin.site.register(Quotation)
admin.site.register(FundRequest)
admin.site.register(Complaint)
admin.site.register(IrrigationOfficer)
admin.site.register(Farmer)
admin.site.register(FarmerComplaint)