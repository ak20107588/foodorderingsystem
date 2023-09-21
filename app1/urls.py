from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.product),
    # path('product1',views.product1),
    path('navbar',views.navbar),
    path('login',views.login),
    path('footer',views.footer),
    path('layout',views.layout),
    path('signup',views.signup_detail),
    path('login_detail',views.login_detail),
    path('logout_view',views.logout_view),
    path('home',views.home),
    path('cart/<str:action>/<int:ProductID>',views.cart),
    path('cart',views.showcart),
    path('checkout',views.checkout),
    path('carosel',views.carosel),
    path('about',views.about),
    path('base',views.base),
    path('UserDetails',views.UserDetails),
    path('confirmorder/<int:UserID>',views.confirmorder),
    path('success/<int:UserID>',views.success),
    path('logout',views.logout),
    # path('remove_cart/<int:ProductID>',views.remove_cart),
    path('clearcart',views.clearcart),
    path('productremove/<int:ProductID>',views.productremove),
    path('profile',views.profile),
    path('delete/<int:id>',views.delete)

    # path('add_to_cart/<int:ProductID>',views.add_to_cart),
    # path('remove_from_cart/<int:ProductID>',views.remove_from_cart)
    # path('cart/add_to_cart/<int:ProductID>/', views.add_to_cart, name='add_to_cart'),
    # path('remove-from-cart/<int:ProductID>/', views.remove_from_cart, name='remove_from_cart'),
    
   
]