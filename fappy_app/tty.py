

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


from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return redirect ('login')



def home(request):
    context ={"Title": 'Index',"Naija": 'Welcome To Index'} 
    return render(request, "home.html", context)



def contact(request):
    context ={"Title": 'Index',"Naija": 'Welcome To Contact'} 
    return render(request, "contact.html", context)





def about(request):
    context ={"Title": 'Index',"Naija": 'Welcome To about'} 
    return render(request, "about.html", context)

def register(request):
    if request.method =="POST":
        register_form = User(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Account Succesful Created, Kindly Login "))
            return redirect('login')
    else:
        register_form = User
    context ={"register_form":register_form}
    return render(request, "register.html", context)



def agobat(request):
    return render(request,"car_inventory_list.html")

def createBrand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_inventory_list')
    else:

        return render(request,"car_inventory_list.html")
    

    
def create_product_view(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        formset = CarModelFormSet(request.POST, instance=product_form.instance)
        
        if product_form.is_valid() and formset.is_valid():
            product = product_form.save()
            formset.instance = product
            formset.save()
            return redirect('home')  # Redirect to the product list or a success page

    else:
        product_form = ProductForm()
        brandform =BrandForm()
        formset = CarModelFormSet()
        ayT=CarModel.objects.all()
        ayo=Brand.objects.all()
        context={'product_form': product_form, 'formset': formset, 'ayT':ayT,'ayo':ayo,'brandform':brandform}

    return render(request, 'create_product.html', context )




def car_inventory_list(request):
    inventory = CarInventory.objects.all()
    return render(request, 'car_inventory_list.html', {'inventory': inventory})


def car_inventory_create(request):
    if request.method == 'POST':
        form = CarInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_inventory_list')
    else:
        form = CarInventoryForm()
    return render(request, 'catalog/car_inventory_form.html', {'form': form})


def car_inventory_update(request, pk):
    inventory = CarInventory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarInventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('car_inventory_list')
    else:
        form = CarInventoryForm(instance=inventory)
    return render(request, 'catalog/car_inventory_form.html', {'form': form})

def car_inventory_delete(request, pk):
    inventory = CarInventory.objects.get(pk=pk)
    if request.method == 'POST':
        inventory.delete()
        return redirect('car_inventory_list')
    return render(request, 'catalog/car_inventory_confirm_delete.html', {'inventory': inventory})

from django.db.models import F

# def inward(request):
    
#    if request.method == 'POST':
       
#        form = TransactionForm(request.POST)
#        if form.is_valid():
#            form.save()

#            return redirect('inward')
#    else:
#     form=TransactionForm()
#     return render(request,'inward.html',{'form': form})


def transaction(request):
   if request.method == 'POST':
       form = TransactionForm(request.POST)
       ay=request.POST.get('vin')
       b=int(ay)
       
       my=request.POST.get('quantity')
       c=int(my)
       inventory = CarInventory.objects.get(id=b)
       if request.POST.get('transaction_type')=='IN':
            inventory.quantity_supplied +=1
            inventory.save()
       elif request.POST.get('transaction_type')!='IN':
           inventory.quantity_sold += 1
           inventory.save()
       context={'inventory':inventory,'my':my,'form': form,'ay': ay}
       return redirect(request,"transaction",context)
   else:
    forms=TransactionForm()
    inventory = 2
    lekan=request.POST
    context={'inventory':inventory,'lekan':lekan,'forms': forms}
    return render(request,'transaction.html',context)


def agobat(request):
    return render(request,"car_inventory_list.html")
