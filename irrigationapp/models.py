from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    userType = models.CharField(max_length=20)


class Sengineer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Jengineer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Overseer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    license = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=20)
    place = models.CharField(max_length=50)
    landmark = models.CharField(max_length=50)
    senior = models.ForeignKey(Sengineer, on_delete=models.CASCADE, null=True)
    junior = models.ForeignKey(Jengineer, on_delete=models.CASCADE, null=True)
    overseer = models.ForeignKey(Overseer, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20)


class Estimation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    duration = models.IntegerField()
    purchase = models.BigIntegerField()
    labour = models.BigIntegerField()
    construction = models.BigIntegerField()
    problem = models.CharField(max_length=200)


class Site(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    other = models.CharField(max_length=100)


class Quotation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    sDate = models.DateField()
    eDate = models.DateField()
    amount = models.CharField(max_length=100)
    quotation = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


class FundRequest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reDate = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


class Complaint(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='Pending')
    senior = models.ForeignKey(Sengineer, on_delete=models.CASCADE, null=True)


class Farmer (models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    land = models.FileField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class IrrigationOfficer(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class FarmerComplaint(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True)
    officer = models.ForeignKey(IrrigationOfficer, on_delete=models.CASCADE, null=True) 
    response = models.CharField(max_length=100, default='Pending')
    responseDate = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='Pending')