from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.db.models import UniqueConstraint 
from django.db.models.functions import Lower
from django.contrib.auth.models import Group
from django.db import models

# class CustomGroup(Group):
#     # Additional fields
#     description = models.CharField(max_length=255)

# class User(AbstractUser,PermissionsMixin):
#     # ...
#     groups = models.ManyToManyField(CustomGroup, related_name='users')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    brand_name  = models.CharField(max_length=100, unique=True,help_text="model name eg Toyota")
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.category.name} ({self.brand_name})"


class Product(models.Model):
    brand_name  = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='Brand_Name')
    category_name  = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='Brand_Name')
    product_name   = models.CharField(max_length=100, unique=True,help_text="model name eg corrolla")
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.brand_name} ({self.product_name})"
     

class Model(models.Model):
    product_name  = models.ForeignKey('Product', on_delete=models.CASCADE)
    model_name    = models.CharField(max_length=100, unique=True,help_text="model name eg Big Daddu")
    model_descr   = models.CharField(max_length=100, unique=True)
    model_SKU     = models.CharField(max_length=100, unique=True)
    date_created = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.product_name} ({self.model_name})"
    

    class Meta:
        ordering = ['product_name','model_name']
        constraints = [UniqueConstraint(Lower('model_name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Model already exists (case insensitive match)" ),]

    

class Customer(models.Model):
    cus_name    = models.CharField(max_length=100, unique=True)
    cust_phone  = models.CharField(max_length=11, unique=True)
    cust_addess    = models.CharField(max_length=100, )
    cust_id    = models.CharField(max_length=100, unique=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.cus_name



class Invoice(models.Model):
    # cus_names = models.OneToOneField(Customer, on_delete=models.CASCADE) 
    invoice_ID    = models.CharField(max_length=100, unique=True)
    tranx_date = models.DateField(default=timezone.now)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.invoice_ID

class Inventory(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    vin = models.CharField(max_length=100, unique=True)
    batch_id = models.CharField(max_length=100)
    balance = models.DecimalField( max_digits=10, decimal_places=1)
    quantity = models.DecimalField( max_digits=10, decimal_places=1, default=0)
    date_supplied = models.DateField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        self.balance += self.quantity
        super().save(*args, **kwargs)  
    
    def __str__(self):
        return f"{self.model} ({self.vin})"

    

class TransactionType(models.TextChoices):
    INWARD = 'IN', 'Inward'
    OUTWARD = 'OUT', 'Outward'   
    SALES = 'Sal', 'Sales'  
    MAINTENANCE = 'Maint', 'Maintenance'    
    

class Transaction(models.Model):
    vin = models.ForeignKey('Inventory', on_delete=models.CASCADE,related_name='transactions')
    cus_Name  = models.ForeignKey('Customer', on_delete=models.CASCADE) 
    invoice_id  = models.ForeignKey('Invoice', on_delete=models.CASCADE) 
    transaction_type = models.CharField(max_length=5, choices=TransactionType.choices,default='IN')
    quantity = models.DecimalField( max_digits=10, decimal_places=1, default=0)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
            return f"{self.cus_Name} ({self.transaction_type})"
   
    def save(self, *args, **kwargs):
        if self.transaction_type == TransactionType.OUTWARD:
            self.quantity = -abs(self.quantity)  # Ensure the quantity is negative
        elif self.transaction_type == TransactionType.SALES:
            self.quantity = -abs(self.quantity)  # Ensure the quantity is positive
        elif self.transaction_type == TransactionType.MAINTENANCE:
            self.quantity = -abs(self.quantity)  # Ensure the quantity is positive
        elif self.transaction_type == TransactionType.INWARD:
            self.quantity = abs(self.quantity)  # Ensure the quantity is positive
        
        # Update the balance
        self.vin.balance += self.quantity
        self.vin.save()

        super().save(*args, **kwargs)
