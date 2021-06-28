from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from .models import *
import datetime
from django.template.loader import get_template 
from django.http import HttpResponse
import random
# Create your views here.
last=product.objects.all()[5:]
def index(request):
    pro= product.objects.all()[:3]
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        return  render(request,"home.html",{"ans":value,"pro":pro,"last":last})
    return render(request,"home.html",{"pro":pro,"last":last})
    
def home(request):
    pro= product.objects.all()
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        items=value.orderitem_set.all()
        context={"items":items,"ans":value,"pro":pro,"last":last}
    else:
        items=[] 
        context={"items":items,"pro":pro,"last":last}
    return render(request,"homepage.html",context)

def login(request):
    if request.method == 'POST':
        pro= product.objects.all()
        username=request.POST["umail"]
        password=request.POST["pass"]
        reg=register.objects.all()
        f=0
        userid=""
        for val in reg:
            if(val.user_email==username and val.user_pass==password):
                userid=val.id
                f=1
        if(f==1):
            request.session['id']=userid
            uid=request.session.get('id')
            cust=customer.objects.get(user_id=uid)
            value, created = order.objects.get_or_create(customer=cust,complete=False)
            items=value.orderitem_set.all()
            return redirect("/")
        else:
            return render(request,"login.html",{"msg":"EMAIL OR PASSWORD WRONG","last":last})
    return render(request,"login.html",{"last":last})
def registers(request):
    if request.method == "POST":
       
        reg=register()
        cust=customer()
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        mail=request.POST["mail"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        cont=request.POST["contact"]
        if pass1==pass2:
            reg.user_fname=fname
            reg.user_lname=lname
            reg.user_email=mail
            reg.user_pass=pass1
            reg.user_contact=cont
            reg.save()
            ans=register.objects.get(user_email=mail)
            cust.name=fname
            cust.email=mail
            cust.user_id=ans.id
            cust.save()
            return render(request,"login.html",{"msg1":"Account Created"})
        else:
            return render(request,"register.html",{"msg":"Something Went Wrong","last":last})
    return render(request,"register.html",{"last":last})

def cartinfo(request):
    data=json.loads(request.body)
    productid=data['productid']
    action=data['action']
    print(productid,"   ",action)
    uid=request.session.get('id')
    cust=customer.objects.get(user_id=uid)
    pro=product.objects.get(id=productid)
    value, created = order.objects.get_or_create(customer=cust,complete=False)
    print(value)
    items, creates =orderitem.objects.get_or_create(order=value,product=pro)
    
    if action=="insert":
        items.quantity=(items.quantity +1 )
    elif action=="remove":
        items.quantity=(items.quantity - 1 )
    items.save()
    if items.quantity<=0:
        items.delete()
    return JsonResponse("Product Added To Your Cart",safe=False)

def cart(request):
    total=0
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        items=value.orderitem_set.all()
        context={"items":items,"ans":value,"last":last}
    else:
        items=[] 
        context={"items":items,"last":last}
    return render(request,"cart.html",context)

def checkout(request):
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        items=value.orderitem_set.all()
        context={"items":items,"ans":value,"last":last}
    else:
        items=[] 
        context={"items":items,"last":last}
    return render(request,"checkout.html",context)

def product_info(request,pid):
    pro=product.objects.get(id=pid)
    context={"pro":pro}
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        items=value.orderitem_set.all()
        context={"items":items,"ans":value,"pro":pro,"last":last}
    else:
        items=[] 
        context={"items":items,"pro":pro,"last":last}
    return render(request,"view.html",context)

def placeorder(request):
    data=json.loads(request.body)
    trans_id=datetime.datetime.now().timestamp()
    print("data")
    if 'id' in request.session:
        uid=request.session.get('id')
        cust=customer.objects.get(user_id=uid)
        value, created = order.objects.get_or_create(customer=cust,complete=False)
        total=float(data["userdetails"]["total"])
        value.transcation_id=random.randint(1500000000, 1600000000)
        if total==value.cart_total:
            value.complete=True
        value.save()

        shipping_details.objects.create(
            customer=cust,
            order=value,
            address=data["shippingdetails"]["address"],
            city= data["shippingdetails"]["city"],
            state=data["shippingdetails"]["state"],
            zipcode=data["shippingdetails"]["code"]
        )
    return JsonResponse("Order completed payment done",safe=False)

def logout(request):
    del request.session['id']
    return redirect("/")
