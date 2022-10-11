from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pwd=request.POST.get('pwd')
        confirmpassword=request.POST.get('confirmpassword')
        if pwd==confirmpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username available")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email available")
                return render(request,"register.html")
            else:
                #To store the value in database
                #Create object for User
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=pwd)
                user.save()
                return render(request,"login.html")
        else:
            messages.info(request,"Password Not matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,"index.html")
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")

    else:
        return render(request,"login.html")