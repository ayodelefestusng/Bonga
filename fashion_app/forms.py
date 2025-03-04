from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import PromoCode
from .models import *


        
          
        
class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']
        labels = {'category': 'Product Category'}  
        

class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
        # fields = [ 'category','name', 'price', 'digital','image']
        # labels = {'category': ' Product Category','name': 'Product Name','price': 'Product Price','digital': 'Digital','image': "Product Image",}  
        

class CurrencyForm (forms.ModelForm):
    class Meta:
        model = Currency
        fields = [ 'naira','pound', 'euro', 'usd']
        labels = {'naira': ' Naira ','pound': 'Pounds ','euro': 'Euro','usd': 'USD'}  




