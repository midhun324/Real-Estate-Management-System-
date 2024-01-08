from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError

from BackEnd.models import Property_details
from FrontEnd.models import TenantDb


# Create your views here.

def index(request):

    return render(request,"index.html")


def admin_loginpage(request):

    return render(request,"admin_login.html")


def adminLogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if User is not None:
                login(request,user)
                request.session["username"]=uname
                request.session["password"]=pwd
                return redirect(index)
            else:
                return redirect(admin_loginpage)

        else:
            return redirect(admin_loginpage)



def AdminLogOut(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)




def add_property(request):
    data=TenantDb.objects.all()

    return render(request,"add_properties.html",{"data":data})


def save_property(request):
    if request.method == "POST":
        pna = request.POST.get("property")
        des = request.POST.get("Description")
        Ty = request.POST.get("type")
        ads = request.POST.get("address")
        pri = request.POST.get("price")
        aria = request.POST.get("area")
        par = request.POST.get("parking")
        gar = request.POST.get("garage")
        sta = request.POST.get("status")
        be = request.POST.get("bed")
        ba = request.POST.get("bath")
        loc = request.POST.get("Loc")
        ty=request.POST.get("type")
        ten=request.POST.get("tenant")

        imag = request.FILES["img"]
        obj = Property_details(PropertyName=pna,Description=des,Type=ty,Address=ads,Price=pri,Size=aria,Parking=par,Garage=gar,PropertyStatus=sta,
                               BedRooms=be,Bathrooms=ba,Image=imag,Location=loc,TenantName=ten,PropertyType=Ty)
        obj.save()
    return redirect(add_property)



def updateProperty(request,dataid):
    if request.method == "POST":
        pna = request.POST.get("property")
        des = request.POST.get("Description")
        Ty = request.POST.get("type")
        ads = request.POST.get("address")
        pri = request.POST.get("price")
        aria = request.POST.get("area")
        par = request.POST.get("parking")
        gar = request.POST.get("garage")
        sta = request.POST.get("status")
        be = request.POST.get("bed")
        ba = request.POST.get("bath")
        loc = request.POST.get("Loc")
        ty = request.POST.get("type")
        ten = request.POST.get("tenant")

        try:
            imag = request.FILES["img"]
            fs = FileSystemStorage()
            file = fs.save(imag.name, imag)
        except MultiValueDictKeyError:
            file = Property_details.objects.get(id=dataid).image
        Property_details.objects.filter(id=dataid).update(PropertyName=pna,Description=des,Type=ty,Address=ads,Price=pri,Size=aria,Parking=par,Garage=gar,PropertyStatus=sta,
                               BedRooms=be,Bathrooms=ba,Image=imag,Location=loc,TenantName=ten,PropertyType=Ty)
        return redirect(show_property)


def show_property(request):
    data=Property_details.objects.all()
    return render(request,"property_details.html",{"data":data})




def editproperty_page(request,dataid):

    data=Property_details.objects.get(id=dataid)
    data1=TenantDb.objects.all()

    return render(request,"edit_property.html",{"data":data,"data1":data1})



def delete_prop(request,dataid):
    data = Property_details.objects.get(id=dataid)

    data.delete()

    return redirect(show_property)



def add_tenant(request):

    return render(request,"add_tenant.html")



def save_tenant(request):
    if request.method == "POST":
        tna = request.POST.get("tname")
        em = request.POST.get("email")
        ph = request.POST.get("phone")
        doc = request.FILES["doc_img"]
        adr = request.POST.get("address")
        timg=request.FILES["tenant_img"]
        obj=TenantDb(Tenant=tna,Phone=ph,Email=em,address=adr,Document_Proofs=doc,
                     ImageTenant=timg)
        obj.save()

        return redirect(add_tenant)


def tenant_details(request):
    data=TenantDb.objects.all()

    return render(request,"tenant_details.html",{"data":data})




def edit_tenant(request,dataid):
    data=TenantDb.objects.get(id=dataid)
    return render(request,"edit_tenant.html",{"data":data})


def updatetenants(request,dataid):
    tna = request.POST.get("tname")
    em = request.POST.get("email")
    ph = request.POST.get("phone")
    doc = request.FILES["doc_img"]
    adr = request.POST.get("address")
    timg = request.FILES["tenant_img"]

    try:
        timg = request.FILES["tenant_img"]
        fs = FileSystemStorage()
        file = fs.save(timg.name, timg)
    except MultiValueDictKeyError:
        file = TenantDb.objects.get(id=dataid).image
    TenantDb.objects.filter(id=dataid).update(Tenant=tna,Phone=ph,Email=em,address=adr,Document_Proofs=doc,
                     ImageTenant=timg)
    return redirect(tenant_details)


def delete_tenants(request,dataid):

    data=TenantDb.objects.get(id=dataid)
    data.delete()

    return redirect(tenant_details)






















