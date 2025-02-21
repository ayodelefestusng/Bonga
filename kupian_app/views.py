


# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages
from .models import PromoCode
from .forms import *
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User



# from django.shortcuts import get_object_o
# r_404, render

# from django.db.models import F
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse



# Create your views here.


def home(request):
    context ={"Title": 'Index',"Naija": 'Welcome To Index'} 
    return render(request, "homes.html", context)



def contact(request):
    context ={"Title": 'Index',"Naija": 'Welcome To Contact'} 
    return render(request, "contact.html", context)



def result(request):
    context ={"Title": 'Index',"Naija": 'Welcome To about'} 
    return render(request, "result.html", context)

def about(request):
    context ={"Title": 'Index',"Naija": 'Welcome To about'} 
    return render(request, "about.html", context)

def todolist(request):
    if request.method =="POST":
       atb= PromoCode(request.POST or None)
       atb.save()
       messages.success(request,("Account Succesful Created, Kindly Login "))
       return render('index')
    
    else:
        ajero =PromoCode.objects.all()
        AjeroT2=User.objects.all()
        AjeroT=User.objects.filter(username="Ayo")
        context ={'Title': 'Index','Naija': 'Welcome To todolist','ajero': ajero,'AjeroT': AjeroT,'AjeroT2': AjeroT2}
        return render(request, "todolist.html", context)



def register(request):
    if request.method =="POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Account Succesful Created, Kindly Login "))
            return redirect('login')
    else:
        register_form = CustomRegisterForm
    context ={"register_form":register_form}
    return render(request, "register.html", context)




def load(request):
     if request.method =="POST":
        register_form = panko(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("Vocuher Loaded Succesfully "))
            return redirect('load')
    
     else:
        register_form = panko
        ajero =CreateGift.objects.all()
        ajeroT =PromoCode.objects.all()
        context ={"Title": 'Index',"Naija": 'Welcome To about',"register_form":register_form,"ajero":ajero,"ajeroT":ajeroT} 
        return render(request, "load.html", context)
    

    
def create_gift(request):
     if request.method =="POST":
        Agaba = CreateeGifts(request.POST or None)
        if Agaba.is_valid():
            Agaba.save()
        messages.success(request,("Gift Created Successfully"))
        return redirect('load')  
    
     else:
        register_form = CreateeGifts
        context ={"Title": 'Index',"Naija": 'Welcome To about',"register_form":register_form} 
        return render(request, "load.html", context)
    
    
# def winnings(request):
#     return render(request, "contact.html")
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return redirect ('login')


def yemi(request):
    return render(request, "contact.html")

def winnings(request):
     if request.method =="POST":
        AgabaT = WinningGiftsG(request.POST or None)
        if AgabaT.is_valid():
            AgabaT.save()
        messages.success(request,("Winning Codes Generarated "))
        return render(request, "load.html")   
    
    #  else:
    #     register_form = CreateeGifts
    #     context ={"Title": 'Index',"Naija": 'Welcome To about',"register_form":register_form} 
    #     return render(request, "load.html", context)   
    

    
    
# def create_gift(request):
#     context ={"Title": 'Index',"Naija": 'Welcome To about'} 
#     return render(request, "about.html", context)    

def redeems (request):
    # Alex=Ajero(request.POST)
    if request.method =="POST":
        # question = get_object_or_404(PromoCode, pk=1)
        # form = panko(request.POST)
        Alex1=PromoCode.objects.filter(status=False).aggregate(sum("gift"))
        Alex2=PromoCode.objects.filter(code=request.POST["agoba"])
        Alex=PromoCode.objects.all()
        context ={'Alex':Alex,'Alex1':Alex1}
        return render(request, "redeem.html", context)
    else:
    
        Alex=PromoCode.objects.all()
        context ={'Alex':Alex}
        return render(request, "redeem.html", context)
    
    
def redeem (request):
    # Alex=Ajero(request.POST)
    if request.method =="POST":
        Alex1=PromoCode.objects.filter(code=request.POST["agoba"])
        task=PromoCode.objects.get(code=request.POST["agoba"])
        task.status=False
        task.save()
        Alex=PromoCode.objects.all()
        context ={'Alex':Alex,'Alex1':Alex1}
        return render(request, "redeem.html", context)
    else:
    
        Alex=PromoCode.objects.all()
        context ={'Alex':Alex}
        return render(request, "redeem.html", context)   
    
    
    
    

from .forms import ValueLookupForm

from django.shortcuts import render, redirect
from .forms import ValueLookupForm
from .models import PromoCode

def value_lookup(request):
    if request.method == 'POST':
        formT = ValueLookupForm(request.POST)
        if formT.is_valid():
            code = formT.cleaned_data['code']
            try:
                obj = PromoCode.objects.get(code=code)
                form = ValueLookupForm()
                context={'id': obj,'form': form,'error': 'Value not found'}
                return render(request, 'lookup.html', context)
            except PromoCode.DoesNotExist:
                form = ValueLookupForm()
                context={'form' : form,'error': 'Value not found'}
                return render(request, 'lookup.html', context)
    else:
        form = ValueLookupForm()
    return render(request, 'lookup.html', {'form': form})

















from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


# def register(request):  
# def register(request):
#     context ={"Title": 'Index',"Naija": 'Welcome To about'} 
#     return render(request, "register.html", context)






# def index(request):
#     latest_question_list = PromoCode.objects.all()
#     context = { "latest_question_list": latest_question_list,    }
#     return render(request, "index.html", context)





# def detail(request, question_id):
#     latest_question_list = PromoCode.objects.filter(gift=question_id).values()
#     # atb = get_object_or_404(PromoCode, gift=question_id)
#     context = { "ayeni": 'ayeni',"latest_question_list": latest_question_list, }
#     return render(request, "detail.html", context)



# # Leave the rest of the views (detail, results, vote) unchanged

# # def detail(request, question_id):
# #     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)




# def load(request):
#     latest_question_list = PromoCode.objects.all()
#     context = { "latest_question_list": latest_question_list,    }
#     return render(request, "load", context)