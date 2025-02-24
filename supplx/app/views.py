from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import os
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import *



# Create your views here.
def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(userprfl)
    if req.method=='POST':
        uname=req.POST['username']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                login(req,data)
                req.session['user']=uname
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
                send_mail('user registration', "Your account has been successfully created. Thank you for joining us!", settings.EMAIL_HOST_USER, [email])     
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
    if 'shop' in req.session:
        product=Product.objects.all()
        return render(req,'shop/shop_home.html',{'data':product})
    else:
        return redirect('shop_login')  # Redirect to the login page if the user is not in the session


def add_pro(req):
    if 'shop' in req.session:
        if req.method=='POST':
            id=req.POST['pro_id']
            name=req.POST['name']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            des=req.POST['des']
            img=req.FILES['img']
            product=Product.objects.create(pro_id=id,name=name,price=price,offer_price=offer_price,des=des,img=img)
            product.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/add_pro.html')
    else:
        return redirect(shop_login)


    
def edit_product(request, pid):
    product = get_object_or_404(Product, pk=pid)
    
    if request.method == 'POST':
        product.pro_id = request.POST.get('pro_id')
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.offer_price = request.POST.get('offer_price')
        product.des = request.POST.get('des')
        
        if 'img' in request.FILES:
            product.img = request.FILES['img']
        
        product.save()
        return redirect(shop_home)  # Redirect to a relevant view after saving

    return render(request, 'shop/edit_pro.html', {'data': product})
    
def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    print(og_path)
    return redirect(shop_home)





#---------------------user----------------------------



    
def user_home(req):
    product=Product.objects.all()
    return render(req,'user/user_home.html',{'data':product})
    
def userprfl(req):
   return render(req,'user/userprfl.html')

def view_pro(req,pid):
    product=Product.objects.get(pk=pid)
    return render(req,'user/view_pro.html',{'data':product})




def prdt(req):
    product=Product.objects.all()
    return render(req,'user/products.html',{'data':product})

def add_to_cart(req,pid):
    if 'user' in req.session:
        prod=Product.objects.get(pk=pid)
        user=User.objects.get(username=req.session['user'])
        data=Cart.objects.create(user=user,product=prod)
        data.save()
        return redirect(view_cart)
    # else:
    #     return redirect(user_home)
    
def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    cart_dtls=Cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart_dtls':cart_dtls})

def delete_cart(req,id):
    cart=Cart.objects.get(pk=id)
    cart.delete()
    return redirect(view_cart)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Send email
        send_mail(
            subject,
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'user/contact.html')
