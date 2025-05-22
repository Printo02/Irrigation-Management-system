from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import *
from django.contrib.auth import authenticate
from django.db.models import Q

######################################################################
#                           LOAD INDEX PAGE
######################################################################


def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "index.html")
######################################################################
#                           LOGIN
######################################################################


def login(request):
    """ 
        The function to load login page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        pwd = request.POST.get("txtPassword")
        user = authenticate(username=email, password=pwd)
        if user is not None:
            request.session['email'] = email
            if user.is_active:
                if user.userType == 'Admin':
                    return HttpResponseRedirect("/adminhome")
                elif user.userType == 'Senior':
                    u = Sengineer.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/sehome")
                elif user.userType == 'Junior':
                    u = Jengineer.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/jehome")
                elif user.userType == "Overseer":
                    u = Overseer.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/overseerhome")
                elif user.userType == "Contractor":
                    u = Contractor.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/contractorhome")
                elif user.userType == "Farmer":
                    u = Farmer.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/farmerhome")
                elif user.userType == "Officer":
                    u = IrrigationOfficer.objects.get(email=email)
                    request.session['uid'] = u.id
                    return HttpResponseRedirect("/officerhome")
            else:
                msg = "You are not authenticated to login"
        else:
            msg = "User doesnt exist"
    return render(request, "login.html", {"msg": msg})
######################################################################
#                       SE REGISTRATION
######################################################################


def seregistration(request):
    """ 
        The function to register senior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]
        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, userType="Senior", is_active=0)
            user.save()
            db = Sengineer.objects.create(
                name=name, phone=contact, email=email, address=address, qualification=qual, user=user)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "seregistration.html", {"msg": msg})
######################################################################
#                       JE REGISTRATION
######################################################################


def jeregistration(request):
    """ 
        The function to register junior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]
        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, userType="Junior", is_active=0)
            user.save()
            db = Jengineer.objects.create(
                name=name, phone=contact, email=email, address=address, qualification=qual, user=user)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "jeregistration.html", {"msg": msg})
######################################################################
#                       OVERSEER REGISTRATION
######################################################################


def overseerregistration(request):
    """ 
        The function to register overseer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, userType="Overseer", is_active=0)
            user.save()
            db = Overseer.objects.create(
                name=name, phone=contact, email=email, address=address, qualification=qual, user=user)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "overseerregistration.html", {"msg": msg})
######################################################################
#                       CONTRACTOR REGISTRATION
######################################################################


def contractorregistration(request):
    """ 
        The function to register contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        licens = request.POST["txtLicense"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, userType="Contractor", is_active=0)
            user.save()
            db = Contractor.objects.create(
                name=name, phone=contact, email=email, address=address, license=licens, user=user)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "contractorregistration.html", {"msg": msg})
######################################################################
#                       COMPLAINT
######################################################################


def complaint(request):
    """ 
        The function to register complaints for public
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        subject = request.POST["txtSubject"]
        desc = request.POST["txtDesc"]

        try:
            db = Complaint.objects.create(
                subject=subject, desc=desc, name=name, address=address, contact=contact)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Your request have been submitted and will process it in 16 days."
    return render(request, "commoncomplaint.html", {"msg": msg})
######################################################################
#                           ADMIN HOME
######################################################################


def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "adminhome.html")
######################################################################
#                           ADMIN SE
######################################################################


def adminse(request):
    """ 
        The function to manage se
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = Sengineer.objects.filter()
    return render(request, "adminse.html", {"data": data})

######################################################################
#                           ADMIN JE
######################################################################


def adminje(request):
    """ 
        The function to manage je
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Jengineer.objects.filter()
    return render(request, "adminje.html", {"data": data})

######################################################################
#                           ADMIN OVERSEER
######################################################################


def adminoverseer(request):
    """ 
        The function to manage overseer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Overseer.objects.filter()
    return render(request, "adminoverseer.html", {"data": data})

######################################################################
#                           ADMIN CONTRACTOR
######################################################################


def admincontractor(request):
    """ 
        The function to manage contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Contractor.objects.filter()
    return render(request, "admincontractor.html", {"data": data})

######################################################################
#                           ADMIN COMPLAINT
######################################################################


def admincomplaint(request):
    """ 
        The function to load contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Complaint.objects.filter(status='Verified').order_by("-id")
    return render(request, "admincomplaint.html", {"data": data})


def adminAssignSe(request):
    id = request.GET['id']
    data = Complaint.objects.get(id=id)
    if request.POST:
        seg = request.POST['seg']
        senior = Sengineer.objects.get(id=seg)
        data.senior = senior
        data.status = 'Assigned'
        data.save()
        return HttpResponseRedirect("/admincomplaint")
    se = Sengineer.objects.all()
    return render(request, "adminAssignSe.html", {"se": se})
######################################################################
#                          ADMIN APPROVE USERS
######################################################################


def adminapproveuser(request):
    """ 
        The function to approve users
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    id = request.GET.get("id")
    status = request.GET.get("status")
    url = request.GET.get("url")
    d = CustomUser.objects.get(id=id)
    d.is_active = status
    d.save()
    return HttpResponseRedirect(url)
######################################################################
#                           ADMIN PROJECT
######################################################################


def adminproject(request):
    """ 
        The function to view projects for approval
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Project.objects.filter(status="submitted")
    return render(request, "adminproject.html", {"data": data})
######################################################################
#                       ADMIN PROJECT ESTIMATION
######################################################################


def adminprojectestimation(request):
    """ 
        The function to view project estimation
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        pid = request.GET.get("id")

        data = Estimation.objects.filter(project__id=pid)
    return render(request, "adminprojectestimation.html", {"data": data})
######################################################################
#                       ADMIN PROJECT ESTIMATION
######################################################################


def adminprojectupdate(request):
    """ 
        The function to view project estimation
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        pid = request.GET.get("id")
        status = request.GET.get("status")

        db = Project.objects.get(id=pid)
        db.status = status
        db.save()
        return HttpResponseRedirect("/adminproject")
######################################################################
#                           ADMIN APPROVED PROJECT
######################################################################


def adminapprovedproject(request):
    """ 
        The function to view approved projects
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Project.objects.filter(status="Approved")
    return render(request, "adminapprovedproject.html", {"data": data})
######################################################################
#                       SE HOME
######################################################################


def sehome(request):
    """ 
        The function to load profile of senior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    data = Sengineer.objects.get(id=uid)
    return render(request, "sehome.html", {"msg": msg, "d": data})


def seProfile(request):
    """ 
        The function to load profile of senior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        try:
            db = Sengineer.objects.get(id=uid)
            db.name = name
            db.address = address
            db.qualification = qual
            db.phone = contact
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"

    data = Sengineer.objects.get(id=uid)
    return render(request, "seProfile.html", {"msg": msg, "d": data})
######################################################################
#                       SE JE
######################################################################


def sejengineer(request):
    """ 
        The function to load junior engineer for se
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Jengineer.objects.filter(user__is_active=1)
    return render(request, "sejengineer.html", {"data": data})
######################################################################
#                       SE OVERSEER
######################################################################


def seoverseer(request):
    """ 
        The function to load overseer for se
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Overseer.objects.filter(user__is_active=1)
    return render(request, "seoverseer.html", {"data": data})
######################################################################
#                       SE CONTRACTOR
######################################################################


def secontractor(request):
    """ 
        The function to load contractor for se
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    data = Contractor.objects.filter(user__is_active=1)
    return render(request, "secontractor.html", {"data": data})
######################################################################
#                           SE COMPLAINT
######################################################################


def secomplaint(request):
    """ 
        The function to load complaint for se
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session['uid']
    data = Complaint.objects.filter(senior__id=uid).order_by("-id")
    return render(request, "secomplaint.html", {"data": data})
######################################################################
#                       SE PROJECT
######################################################################


def seproject(request):
    """ 
        The function to add project plan
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        desc = request.POST["txtDesc"]
        place = request.POST["txtPlace"]
        landmark = request.POST["txtLandmark"]
        se = Sengineer.objects.get(id=uid)
        try:
            db = Project.objects.create(
                name=name, desc=desc, place=place, landmark=landmark, senior=se, status='pending')
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            return HttpResponseRedirect(f"/seselectje?pid={db.id}")

    return render(request, "seproject.html", {"msg": msg})
######################################################################
#                           SE SELECT JE
######################################################################


def seselectje(request):
    """ 
        The function to select je for project cost estimation
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    pid = request.GET['pid']
    data = Jengineer.objects.filter(user__is_active=1)
    return render(request, "seselectjec.html", {"data": data, "pid": pid})
######################################################################
#                           SE JE
######################################################################


def seje(request):
    """ 
        The function to select je for project
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        jeid = request.GET.get("id")
        pid = request.GET.get("pid")
        pro = Project.objects.get(id=pid)
        je = Jengineer.objects.get(id=jeid)
        pro.junior = je
        pro.save()
        return HttpResponseRedirect(f"/seselectoverseer?pid={pid}")
######################################################################
#                           SE SELECT OVERSEER
######################################################################


def seselectoverseer(request):
    """ 
        The function to select overseer for project 
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    pid = request.GET['pid']
    data = Overseer.objects.filter(user__is_active=1)
    return render(request, "seselectoverseer.html", {"data": data, "pid": pid})
######################################################################
#                           SE OVERSEER
######################################################################


def seos(request):
    """ 
        The function to select overseer for project
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        id = request.GET.get("id")
        pid = request.GET.get("pid")
        pro = Project.objects.get(id=pid)
        ov = Overseer.objects.get(id=id)
        pro.overseer = ov
        pro.save()
        return HttpResponseRedirect("/seprojectforestimation")
######################################################################
#                       SE PROJECT FOR ESTIMATION
######################################################################


def seprojectforestimation(request):
    """ 
        The function to view project for cost estimation
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = Project.objects.filter(senior=uid, status='pending')
    return render(request, "seprojectforestimation.html", {"data": data})
######################################################################
#                       SE PROJECT STATUS
######################################################################


def seprojectstatus(request):
    """ 
        The function to view project status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = Project.objects.filter(senior=uid).exclude(status='pending')
    return render(request, "seprojectstatus.html", {"data": data})
######################################################################
#                       SE PROJECT ESTIMATION
######################################################################


def seprojectestimation(request):
    """ 
        The function to view project estimation for se
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        pid = request.GET.get("id")
        data = Estimation.objects.filter(project__id=pid)
    return render(request, "seprojectestimation.html", {"data": data})
######################################################################
#                       SE APPROVED PROJECT
######################################################################


def seapprovedproject(request):
    """ 
        The function to view project status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = Project.objects.filter(senior=uid, status='Approved')
    return render(request, "seapprovedprojects.html", {"data": data})
######################################################################
#                       SE FUND REQUEST
######################################################################


def sefundrequest(request):
    """ 
        The function to view fund request for SE
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = FundRequest.objects.filter(
        project__senior__id=uid, status='Approved by JE')
    return render(request, "sefundrequest.html", {"data": data})
######################################################################
#                       JE FUND REQUEST UPDATE
######################################################################


def sefundrequestupdate(request):
    """ 
        The function to view fund request for SE
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    rid = request.GET.get("id")
    status = request.GET.get("status")
    db = FundRequest.objects.get(id=rid)
    db.status = status
    db.save()
    return HttpResponseRedirect("/sefundrequest")
######################################################################
#                       SE QUOTATIONS
######################################################################


def sequotations(request):
    """ 
        The function to view quotation status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    data = Quotation.objects.filter(
        project__senior__id=uid, status='submitted')
    return render(request, "sequotations.html", {"data": data})
######################################################################
#                       SE QUOTATIONS UPDATE
######################################################################


def sequotationupdate(request):
    """ 
        The function to view quotation status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    if(request.GET):
        qid = request.GET.get("id")
        status = request.GET.get("status")

        db = Quotation.objects.get(id=qid)
        db.status = status
        db.save()
    return HttpResponseRedirect("/sequotations")
######################################################################
#                       JE HOME
######################################################################


def jehome(request):
    """ 
        The function to load profile of junior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    d = Jengineer.objects.get(id=uid)
    return render(request, "jehome.html", {"msg": msg, "d": d})


def jeProfile(request):
    """ 
        The function to load profile of junior engineer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        try:
            db = Jengineer.objects.get(id=uid)
            db.name = name
            db.address = address
            db.phone = contact
            db.qualification = qual
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"

    d = Jengineer.objects.get(id=uid)
    return render(request, "jeProfile.html", {"msg": msg, "d": d})
######################################################################
#                       JE PROJECT FOR ESTIMATION
######################################################################


def jeprojectforestimation(request):
    """ 
        The function to view project for cost estimation
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = Project.objects.filter(junior__id=uid, status='pending')
    return render(request, "jeproject.html", {"data": data})
######################################################################
#                       JE COST ESTIMATION
######################################################################


def jecostestimation(request):
    """ 
        The function to add cost estimation
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    pid = request.GET.get("id")
    if Estimation.objects.filter(project__id=pid).exists():
        return HttpResponseRedirect("/jeprojectforestimation")
    if(request.POST):
        duration = request.POST["txtDuration"]
        purchase = request.POST["txtPcost"]
        labor = request.POST["txtLcost"]
        construction = request.POST["txtCcost"]
        problem = request.POST["txtProblem"]
        try:
            pro = Project.objects.get(id=pid)
            db = Estimation.objects.create(
                project=pro, duration=duration, purchase=purchase, labour=labor, construction=construction, problem=problem)
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            try:
                pro.status = 'estimated'
                pro.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Estimation added successfully"

    return render(request, "jecostestimation.html", {"msg": msg})
######################################################################
#                       JE FUND REQUEST
######################################################################


def jefundrequest(request):
    """ 
        The function to view fund request for JE
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = FundRequest.objects.filter(
        project__junior__id=uid, status='requested')
    return render(request, "jefundrequest.html", {"data": data})
######################################################################
#                       JE FUND REQUEST UPDATE
######################################################################


def jefundrequestupdate(request):
    """ 
        The function to view fund request for JE
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    rid = request.GET.get("id")
    status = request.GET.get("status")

    db = FundRequest.objects.get(id=rid)
    db.status = status
    db.save()
    return HttpResponseRedirect("/jefundrequest")
######################################################################
#                       OVERSEER HOME
######################################################################


def overseerhome(request):
    """ 
        The function to load profile of overseer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    data = Overseer.objects.get(id=uid)
    return render(request, "overseerhome.html", {"msg": msg, "d": data})


def osProfile(request):
    """ 
        The function to load profile of overseer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        try:
            db = Overseer.objects.get(id=uid)
            db.name = name
            db.address = address
            db.phone = contact
            db.qualification = qual
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"

    data = Overseer.objects.get(id=uid)
    return render(request, "osProfile.html", {"msg": msg, "d": data})
######################################################################
#                       OS PROJECT FOR ESTIMATION
######################################################################


def osprojectforsite(request):
    """ 
        The function to view project for site registration
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = Project.objects.filter(Q(overseer__id=uid) & Q(
        Q(status='pending') | Q(status='estimated')))
    return render(request, "osprojectforsite.html", {"data": data})
######################################################################
#                       OS SITE
######################################################################


def ossite(request):
    """ 
        The function to view project for site registration
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    pid = ""
    if(request.GET):
        pid = request.GET.get("id")
        if Site.objects.filter(project__id=pid).exists():
            return HttpResponseRedirect("/osprojectforsite")
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        other = request.POST["txtOther"]
        try:
            pro = Project.objects.get(id=pid)
            db = Site.objects.create(
                project=pro, name=name, address=address, other=other)
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            try:
                pro.status = 'submitted'
                pro.save()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Estimation added successfully"

    return render(request, "ossite.html", {"msg": msg})
######################################################################
#                       OS APPROVED PROJECT
######################################################################


def osapprovedproject(request):
    """ 
        The function to view approved project
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = Project.objects.filter(overseer__id=uid, status='Approved')
    return render(request, "overseerapprovedprojects.html", {"data": data})
######################################################################
#                       OS REQUEST FUND
######################################################################


def osfundrequest(request):
    """ 
        The function to add fund request
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""

    pid = ""
    if(request.GET):
        pid = request.GET.get("id")
    if(request.POST):
        amt = request.POST["txtAmt"]
        try:
            pro = Project.objects.get(id=pid)
            db = FundRequest.objects.create(
                project=pro, amount=amt, status='requested')
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Fund requested"
    return render(request, "osfundrequest.html", {"msg": msg})
######################################################################
#                       OS REQUEST FUND STATUS
######################################################################


def osfundrequeststatus(request):
    """ 
        The function to view fund request
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = FundRequest.objects.filter(project__overseer__id=uid)
    return render(request, "osfundrequeststatus.html", {"data": data})
######################################################################
#                       OS Complaints
######################################################################


def osComplaint(request):
    """ 
        The function to view complaints
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = Complaint.objects.all().order_by("-id")
    return render(request, "osComplaint.html", {"data": data})


def osConComp(request):
    id = request.GET['id']
    status = request.GET['status']
    data = Complaint.objects.get(id=id)
    data.status = status
    data.save()
    return HttpResponseRedirect("/osComplaint")
######################################################################
#                       CONTRACTOR HOME
######################################################################


def contractorhome(request):
    """ 
        The function to load profile of contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    data = Contractor.objects.get(id=uid)
    return render(request, "contractorhome.html", {"msg": msg, "d": data})


def coProfile(request):
    """ 
        The function to load profile of contractor
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        try:
            db = Contractor.objects.get(id=uid)
            db.name = name
            db.address = address
            db.phone = contact
            db.license = qual
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"
    data = Contractor.objects.get(id=uid)
    return render(request, "coProfile.html", {"msg": msg, "d": data})
######################################################################
#                       CONTRACTOR PROJECT
######################################################################


def contractorproject(request):
    """ 
        The function to view project for contractors
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    qts = Quotation.objects.filter(Q(status='Approved') | Q(status='approved'))

    data = Project.objects.filter(status='Approved').exclude(id__in=[q.project.id for q in qts])
    return render(request, "contractorproject.html", {"data": data})
######################################################################
#                       CONTRACTOR QUOTATION
######################################################################


def contractorquotation(request):
    """ 
        The function to add quotation
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.GET):
        pId = request.GET.get("id")
    if(request.POST):
        sdate = request.POST["txtSdate"]
        edate = request.POST["txtEdate"]
        amt = request.POST["txtAmt"]
        quotation = request.POST["txtQuotation"]
        try:
            pro = Project.objects.get(id=pId)
            con = Contractor.objects.get(id=uid)
            db = Quotation.objects.create(project=pro, contractor=con, sDate=sdate,
                                          eDate=edate, amount=amt, quotation=quotation, status='submitted')
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Quotation submitted"
    return render(request, "contractorquotation.html", {"msg": msg})
######################################################################
#                       CONTRACTOR QUOTATIONS
######################################################################


def contractorquots(request):
    """ 
        The function to view quotation status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = Quotation.objects.filter(contractor__id=uid)
    return render(request, "contractorquots.html", {"data": data})


def farmerregistration(request):
    """ 
        The function to register farmer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        email = request.POST["txtEmail"]
        land = request.FILES["txtLand"]
        password = request.POST["txtPassword"]

        try:
            user = CustomUser.objects.create_user(
                username=email, password=password, userType="Farmer", is_active=1)
            user.save()
            db = Farmer.objects.create(
                name=name, phone=contact, email=email, address=address, user=user, land=land)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "farmerregistration.html", {"msg": msg})

def officerregistration(request):
    """ 
        The function to register officer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        email = request.POST["txtEmail"]
        pwd = request.POST["txtPassword"]

        try:
            user = CustomUser.objects.create_user(
                username=email, password=pwd, userType="Officer", is_active=0)
            user.save()
            db = IrrigationOfficer.objects.create(
                name=name, phone=contact, email=email, address=address, qualification=qual, user=user)
            db.save()
        except:
            msg = "Sorry registration error"
        else:
            msg = "Registration successfull"
    return render(request, "officerregistration.html", {"msg": msg})

def adminfarmer(request):
    """ 
        The function to manage farmer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = Farmer.objects.filter()
    return render(request, "adminfarmer.html", {"data": data})

def adminofficer(request):
    """ 
        The function to manage officer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = IrrigationOfficer.objects.filter()
    return render(request, "adminofficer.html", {"data": data})

def adminviewfarmercomplaint(request):
    """ 
        The function to view farmer complaints
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """

    data = FarmerComplaint.objects.filter().order_by("-id")
    return render(request, "adminviewfarmercomplaint.html", {"data": data})


def farmerhome(request):
    """ 
        The function to load profile of farmer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    data = Farmer.objects.get(id=uid)
    return render(request, "farmerhome.html", {"msg": msg, "d": data})

def farmerComplaint(request):
    """ 
        The function to add complaint
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        subject = request.POST["txtSubject"]
        desc = request.POST["txtDesc"]
        try:
            farmer = Farmer.objects.get(id=uid)
            db = FarmerComplaint.objects.create(
                farmer=farmer, subject=subject, desc=desc)
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Complaint submitted"
    return render(request, "farmerComplaint.html", {"msg": msg})

def farmerViewComplaint(request):
    """ 
        The function to view complaints
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = FarmerComplaint.objects.filter(farmer__id=uid).order_by("-id")
    return render(request, "farmerViewComplaint.html", {"data": data})

def farmerProfile(request):
    """ 
        The function to load profile of farmer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        try:
            db = Farmer.objects.get(id=uid)
            db.name = name
            db.address = address
            db.phone = contact
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"
    data = Farmer.objects.get(id=uid)
    return render(request, "farmerProfile.html", {"msg": msg, "d": data})

def officerhome(request):
    """ 
        The function to load profile of officer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]

    data = IrrigationOfficer.objects.get(id=uid)
    return render(request, "officerhome.html", {"msg": msg, "d": data})

def officerComplaint(request):
    """ 
        The function to view complaints
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = FarmerComplaint.objects.filter(status='Pending').order_by("-id")
    return render(request, "officerComplaint.html", {"data": data})

def officerUpdateComplaintStatus(request):
    """ 
        The function to update complaint status
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]
    officer = IrrigationOfficer.objects.get(id=uid)
    id = request.GET['id']
    status = request.GET['status']
    data = FarmerComplaint.objects.get(id=id)
    data.status = status
    data.officer = officer
    data.save()
    if  status == 'Responded':
        return HttpResponseRedirect("/officerComplaintRespond?id="+id)
    return HttpResponseRedirect("/officerComplaint")

def officerComplaintRespond(request):
    """ 
        The function to respond to complaints
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    id = request.GET['id']
    data = FarmerComplaint.objects.get(id=id)
    if request.POST:
        response = request.POST['txtResponse']
        data.response = response
        data.save()
        return HttpResponseRedirect("/officerComplaint")
    return render(request, "officerComplaintRespond.html", {"data": data})

def officerComplaintHistory(request):
    """ 
        The function to view complaints
        -----------------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    uid = request.session["uid"]

    data = FarmerComplaint.objects.filter(status='Responded',officer__id=uid).order_by("-id")
    return render(request, "officerComplaintHistory.html", {"data": data})

def officerProfile(request):
    """ 
        The function to load profile of officer
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    msg = ""
    uid = request.session["uid"]
    if(request.POST):
        name = request.POST["txtName"]
        address = request.POST["txtAddress"]
        contact = request.POST["txtContact"]
        qual = request.POST["txtQual"]
        try:
            db = IrrigationOfficer.objects.get(id=uid)
            db.name = name
            db.address = address
            db.phone = contact
            db.qualification = qual
            db.save()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Updation successfull"
    data = IrrigationOfficer.objects.get(id=uid)
    return render(request, "officerProfile.html", {"msg": msg, "d": data})


def about(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 

        Returns: 
            html page
    """
    return render(request, "about.html")