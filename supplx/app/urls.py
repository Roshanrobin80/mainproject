from django.urls import path
from . import views


urlpatterns=[
    path('',views.user_home),
    path('shop_logout',views.shop_logout),
    path('shop_login',views.shop_login),



# --------------------shop--------------------
    path('shop_home',views.shop_home),
    path('add_pro',views.add_pro),  




#---------------------user-----------------------
    path('register',views.register),
    # path('user_home',views.user_home),
    path('userprfl',views.userprfl),
    path('view_pro/<pid>',views.view_pro),



]