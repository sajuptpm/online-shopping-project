from django.shortcuts import render

# Create your views here.

from book.models import Usertb
from book.models import Catagorytb
from book.models import Producttb
from book.models import Carttb
from book.forms import UserRegistrationForm
from book.forms import LoginForm
from book.forms import  ProductForm
from django.http import HttpResponse

def add_user(request):
    
    #object creation
    #print  " get msg",request.GET
    #print  " post msg",request.POST
    if request.method == 'GET':
        form = UserRegistrationForm()
        #print "hai"
    else:
        #print "POST"
        p=Usertb(uname=request.POST.get('uname'),password=request.POST.get('password'),emailid=request.POST.get('emailid'),mobile=request.POST.get('mobile'))
        p.save()
        
        return HttpResponse("Form submitted")
        
    return render(request, 'registration.html', {'form': form,})

def login_user(request):
    #print "hai"
    
    if request.method == 'GET': 
        form = LoginForm()
    else:
        return HttpResponse("LOG IN")
    return render(request, 'login.html', {'form': form,})

def add_product(request):
  
    if request.method == 'GET':
        form = ProductForm()
    else:
        return HttpResponse("PRODUCT ADDED")
    return render(request, 'addproduct.html', {'form':form})





