from django.shortcuts import render,redirect

from BackEnd.models import Property_details
from FrontEnd.models import TenantDb, signupdb
from django.contrib import messages


# Create your views here.


def homepage(request):

    data3=Property_details.objects.all()
    data4=TenantDb.objects.all()

    return render(request,"homepage.html",{"data3":data3,"data4":data4})


def tenant_singlepage(request,Tname):
    data4 = TenantDb.objects.all()
    tenantdata=Property_details.objects.filter(TenantName=Tname)

    return render(request,"tenant_singlepage.html",{"data4":data4,"tenantdata":tenantdata})



def property_page(request):
    data=Property_details.objects.all()
    data4 = TenantDb.objects.all()

    return render(request,"poperty_page.html",{"data":data,"data4":data4})


def property_singlepage(request,dataid):
    data=Property_details.objects.get(id=dataid)
    data4 = TenantDb.objects.all()
    return render(request,"property_singlepage.html",{"data":data,"data4":data4})


def blogpage(request):
    data4 = TenantDb.objects.all()


    return render(request,"blogpage.html",{"data4":data4})


def aboutpage(request):
    data4 = TenantDb.objects.all()

    return render(request,"aboutpage.html",{"data4":data4})

def contactpage(request):
    data4 = TenantDb.objects.all()


    return render(request,"contact.html",{"data4":data4})



def login_register(request):


    return render(request,"Login_register.html")




def save_signup(request):
    if request.method=="POST":
        na=request.POST.get("fullname")
        em=request.POST.get("email")
        pwd=request.POST.get("password")
    obj=signupdb(name=na,email=em,password=pwd)
    obj.save()
    return redirect(login_register)


def UserLogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        if signupdb.objects.filter(name=uname,password=pwd).exists():
            request.session["username"]=uname
            request.session["password"]=pwd
            messages.success(request, "Sucessfully Log In")
            return redirect(homepage)
        else:
            messages.error(request, "invalid Username or Password")
            return redirect(login_register)
        messages.error("invalid Username or Password")
    return redirect(login_register)


def user_Logout(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(login_register)


