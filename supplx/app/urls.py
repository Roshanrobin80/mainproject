from django.urls import path
from . import views


urlpatterns=[
    path('',views.shop_login),
    path('register',views.register),
    path('admin_home',views.admin_home),
    path('user_home',views.user_home),

]