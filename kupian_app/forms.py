from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import PromoCode
from .models import *

class CustomRegisterForm (UserCreationForm):
    email =forms.EmailField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
        
class panko (forms.ModelForm):
    
    class Meta:
        model = PromoCode
        fields = ['code','gift']
        

class CreateeGifts (forms.ModelForm):
    class Meta:
        model = CreateGift
        fields = ['gift_name','value','QuantityProduced','gift_picture']       
        

class WinningGiftsG (forms.ModelForm):
    class Meta:
        model =Winning_Code
        fields = ['items_name','Voucher_id']   





class Ajero (forms.ModelForm):
    
    class Meta:
        model = PromoCode
        fields = ['code']

## MetaAI
from django import forms
# from .models import MyModel

class ValueLookupForm(forms.Form):
    code = forms.CharField(max_length=255)





from django import forms
from .models import Product
# from crispy_forms.helper import FormHelper

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['code_id', 'point', 'gift_picture', 'image']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
