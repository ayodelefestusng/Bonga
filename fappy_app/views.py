

# Create your views here.
from .forms import *
from .models import *

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return redirect ('login')


def home(request):
    context ={"Title": 'Top Power Systems',"Naija": 'Welcome To Index'} 
    return render(request, "home.html", context)


def contact(request):
    context ={"Title": 'Index',"Naija": 'Welcome To Contact'} 
    return render(request, "contact.html", context)


def about(request):
    context ={"Title": 'Index',"Naija": 'Our Team'} 
    return render(request, "about.html", context)

# def register(request):
#     if request.method =="POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#         messages.success(request,("Account Succesful Created, Kindly Login "))
#         return redirect('about')
#     else:
#         register_form = CustomUserCreationForm
#     context ={"register_form":register_form}
#     return render(request, "register.html", context)


def category(request):
        if request.method =="POST":
             catgeory = CategoryForm(request.POST or None)
             if catgeory.is_valid ():
                 catgeory.save()
             messages.success(request,("Category Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            category = CategoryForm
            context ={"category":category}
            return redirect(request, "admin.html", context)


def brand(request):
        if request.method =="POST":
             brand = BrandForm(request.POST or None)
             if brand.is_valid ():
                 brand.save()
             messages.success(request,("Product Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            brand = BrandForm
            context ={"brand":brand}
            return redirect(request, "admin.html", context)

def product(request):
        if request.method =="POST":
             product = ProductForm(request.POST or None)
             if product.is_valid ():
                 product.save()
             messages.success(request,("Product Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            product = ProductForm
            context ={"product":product}
            return redirect(request, "admin.html", context)
            


def model(request):
        if request.method =="POST":
             model = ModelForm(request.POST or None)
             if model.is_valid ():
                 model.save()
             messages.success(request,("Model Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            model = ModelForm
            context ={"model":model}
            return redirect(request, "admin.html", context)
        
        
def customer(request):
        if request.method =="POST":
             customer = CustomerForm(request.POST or None)
             if customer.is_valid ():
                 customer.save()
             messages.success(request,("Customer Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            customer = ModelForm
            context ={"customer":customer}
            return redirect(request, "admin.html", context)
               

def invoice(request):
        if request.method =="POST":
             invoice = InvoiceForm(request.POST or None)
             if invoice.is_valid ():
                 invoice.save()
             messages.success(request,("Invoice Succesful Created, Kindly Login "))
           
             return redirect('admin')

        else:
            invoice = InvoiceForm
            context ={"invoice":invoice}
            return redirect(request, "admin.html", context)      
        
        

def admin(request):
        if request.method =="POST":
             brand = BrandForm(request.POST or None)
             if brand.is_valid ():
                 brand.save()
             messages.success(request,("Brand Succesful Created, Kindly Login "))
             return redirect('admin')

        else:
            brand = BrandForm
            category = CategoryForm
            product = ProductForm
            model = ModelForm
            customer = CustomerForm
            invoice = InvoiceForm
            inventory = InventoryForm
            aye='aye'
            context ={"brand":brand,'category':category,'aye':aye,'product':product,'model':model,
                      'customer':customer,'invoice':invoice,'inventory':inventory,}
            return render(request, "admin.html", context)
            
def inventory(request):
        if request.method =="POST":
             inventory = InventoryForm(request.POST or None)
             if inventory.is_valid ():
                 inventory.save()
             messages.success(request,("Invoice Succesful Created, Kindly Login "))
           
             return redirect('dailyops')

        else:
            inventory = InventoryForm
            context ={"inventory":inventory}
            return redirect(request, "dailyops.html", context)      
        
        
def transaction(request):
        if request.method =="POST":
             transaction = TransactionForm(request.POST or None)
             if transaction.is_valid ():
                 transaction.save()
             messages.success(request,("Invoice Succesful Created, Kindly Login "))
           
             return redirect('dailyops')

        else:
            transaction = TransactionForm
            context ={"inventory":inventory}
            return redirect(request, "dailyops.html", context)      


def dailyops(request):
        if request.method =="POST":
             inventory = InventoryForm(request.POST or None)
             if inventory.is_valid ():
                 inventory.save()
             messages.success(request,("Invoice Succesful Created, Kindly Login "))
           
             return redirect('dailyops')

        else:
        
            inventory = InventoryForm
            transaction = TransactionForm
            aye='aye'
            transact_report=Transaction.objects.all()
            u = User.objects.all()
            context ={'inventory':inventory,'transaction':transaction,'transact_report':transact_report,' u': u}
            return render(request, "dailyops.html", context)


from django.contrib.auth.models import User
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

def del_user(request, username):    

        u = User.objects.get(username = 'Folake')
        u.delete()
        return render(request, "dailyops.html")
