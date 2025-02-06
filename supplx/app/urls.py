from django.urls import path
from . import views


urlpatterns=[
    path('',views.user_home),
    path('shop_logout',views.shop_logout),
    path('shop_login',views.shop_login),



# --------------------admin--------------------
    path('shop_home',views.shop_home),
    path('add_pro',views.add_pro),  
    path('edit_product/<pid>',views.edit_product),





#---------------------user-----------------------
    path('register',views.register),
    path('userprfl',views.userprfl),
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('prdt',views.prdt),
    path('user_home',views.user_home),






]