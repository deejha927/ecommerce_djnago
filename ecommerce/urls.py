from django.urls import path
from . import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("",views.home,name="home"),
    path("login",views.login,name="login"),
    path("reg",views.registers,name="reg"),
    path("cart",views.cart,name="cart"),
    path("check",views.checkout,name="check"),
    path("addtocart",views.cartinfo,name="addtocart"),
    path("view_info/<str:pid>/",views.product_info,name="view_info"),
    path("placeorder",views.placeorder,name="placeorder"),
    path("logout",views.logout,name="logout"),
    path("nav",views.navbar,name="nav"),

    ]