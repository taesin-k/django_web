from django.shortcuts import render,get_object_or_404
from .models import User,Product

# Create your views here.

def index(request):
    return render(request,'user/index.html')

def mall(request):
    #products=Product.objects
    return render(request, 'user/mall.html')

def information(request):
    users=User.objects
    return render(request, 'user/information.html',{'users':users})

def search(request):
    return render(request, 'user/search.html')

def detail(request,user_id):
    user=get_object_or_404(User,pk=user_id)
    return render(request,'user/detail.html',{'user':user})

def product_detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'user/product_detail.html',{'product':product})

def pay(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'user/pay.html',{'product':product})
