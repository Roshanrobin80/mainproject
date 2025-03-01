from django.urls import path
from . import views


urlpatterns=[
    path('',views.user_home),
    path('shop_logout',views.shop_logout),
    path('shop_login',views.shop_login),



# --------------------admin--------------------
    path('shop_home',views.shop_home),
    path('add_pro',views.add_pro),  
    path('edit_product/<int:pid>/', views.edit_product, name='edit_product'),
    path('delete_product/<pid>',views.delete_product),






#---------------------user-----------------------
    path('register',views.register),
    path('userprfl',views.userprfl),
    path('view_pro/<pid>',views.view_pro),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    # path('update_cart/<int:cart_id>/', views.update_cart, name='update_cart'),  # Add this line
    path('delete_cart/<id>',views.delete_cart),
    path('prdt',views.prdt),
    path('user_home',views.user_home),
    path('contact/', views.contact, name='contact'),
    path('user_buy1/<pid>',views.user_buy1),
    path('user_buy/<cid>',views.user_buy),









]