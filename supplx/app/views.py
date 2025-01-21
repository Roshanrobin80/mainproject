from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import os
from django.contrib import messages
from .models import *



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
                return redirect(shop_home)
            else:
                login(req,data)
                # req.session['user']=uname
                return redirect(user_home)
        else:
            messages.warning(req,"Invalid uname or password")
            return redirect(shop_login)
    else:
        return render(req,'login.html')
    
def shop_logout(req):
    req.session.flush()
    logout(req)
    return redirect(shop_login)
    
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


def shop_home(req):
    return render(req,'shop/shop_home.html')

def add_pro(req):
    # if 'shop' in req.session:
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']
        price=req.POST['price']
        offer_price=req.POST['offer_price']
        des=req.POST['des']
        img=req.FILES['img']
        data=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,des=des,img=img)
        data.save()
        return redirect(shop_home)
    else:
        return render(req,'shop/add_pro.html')
    # else:
    #     return redirect(shop_login)


def edit_product(req,pid):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            des=req.POST['des']
            img=req.FILES['img']
            if img:
                Product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,dis=des,img=img)
            else:
                Product.objects.filter(pk=pid).update(pro_id=id,name=name,price=price,offer_price=offer_price,dis=des)

            return redirect(shop_home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit_pro.html',{'product':data})
    else:
        return redirect(shop_login)





#---------------------user----------------------------



def user_home(req):
    # if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/user_home.html',{'data':data})
    # else:
    #     return redirect(shop_login)
    
def userprfl(req):
   return render(req,'user/userprfl.html')

def view_pro(req,pid):
    data=Product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':data})



    # return render(req,'user/user_home.html')

def add_to_cart(req,pid):
    if 'user' in req.session:
        prod=Product.objects.get(pk=pid)
        user=User.objects.get(username=req.session['user'])
        data=Cart.objects.create(user=user,product=prod)
        data.save()
        return redirect(viewcart)
    else:
        return redirect(user_home)
