from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import os
from django.contrib import messages



# Create your views here.
def shop_login(req):
    if req.method=='POST':
        uname=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                # req.session['shop']=uname~
                return redirect(admin_home)
            else:
                login(req,data)
                # req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid uname or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    
def register(req):
        if req.method=='POST':
            name=req.POST['name']
            email=req.POST['email']
            password=req.POST['password']
            try:
                data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
                data.save()
                return redirect(shop_login)
            except:
                messages.warning(req,"Email already exist")
                return redirect(register)
        else:
            return render(req,'user/register.html')



#----------------------admin--------------------------


def admin_home(req):
    return render(req,'admin/admin_home.html')





#---------------------user----------------------------



def user_home(req):
    return render(req,'user/user_home.html')