from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path("products",views.home,name="home"),
    path("",views.index,name="home"),
    path("login",views.login,name="login"),
    path("reg",views.registers,name="reg"),
    path("cart",csrf_exempt(views.cart),name="cart"),
    path("check",views.checkout,name="check"),
    path("addtocart",csrf_exempt(views.cartinfo),name="addtocart"),
    path("view_info/<str:pid>/",views.product_info,name="view_info"),
    path("placeorder",csrf_exempt(views.placeorder),name="placeorder"),
    path("logout",views.logout,name="logout"),

    ]