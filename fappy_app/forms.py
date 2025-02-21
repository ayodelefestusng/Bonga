from django import forms
from django.forms import inlineformset_factory
from .models import *


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field
from django.contrib.auth.forms import UserCreationForm

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         # fields = ('username', 'email', 'password1','password2')
#         fields = ('username', 'email', 'password')






# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')  # Add any other fields you need

#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'  # Add any custom styles or classes


        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['category','brand_name']
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand_name','category_name','product_name']
        labels = {'brand_name': 'Brand Name ','category_name': 'Categoary Name','product_name': 'Product Name'}
        

class ModelForm(forms.ModelForm):
    class Meta:
        model = Model
        fields = [ 'product_name', 'model_name','model_descr','model_SKU']
        widgets = {'model_name': forms.TextInput(attrs={'placeholder': 'Year or Model Number'}), 'model_descr': forms.TextInput(attrs={'placeholder': 'Description of Model'}),    }
        labels = {'model_name': 'Model Number','model_descr': 'Modele Info','model_SKU': 'SKU'}

CarModelFormSet = inlineformset_factory(Product, Model, form=ModelForm, extra=1 , can_delete=False )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['cus_name','cust_phone','cust_addess','cust_id']
        labels = {'cus_name': 'Customer Name','cust_phone': 'Customer Phone','cust_addess': 'Address','cust_id': 'Customer ID'}
        
        
        
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_ID','tranx_date',]
        labels = {'invoice_ID': 'Invoice Number','tranx_date': 'Transaction Date'}
        
        
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['model','vin','batch_id','quantity','balance']
        labels = {'model': 'Model Number','vin': 'VIN','quantity': 'Quantity','batch_id': 'Invoice Number','balance': 'Stock Balance',}    
        
        
        
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
        exclude =['created']
