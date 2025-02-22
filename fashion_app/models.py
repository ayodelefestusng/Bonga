from django.db import models
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Category(models.Model):
	category = models.CharField((""), max_length=50,  )
	def __str__(self):
		return self.category

class Product(models.Model):
	category = models.ForeignKey('Category', verbose_name=(""), on_delete=models.CASCADE, null=True,default= "")
	name = models.CharField(max_length=200)
	price = models.PositiveIntegerField((""))
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

  
	def __str__(self):
		return self.name

	@property
	def get_currency_value(self, currency_code):
		"""Fetch the exchange rate from the Currency model based on selected currency."""
		try:
			currency = Currency.objects.get(currency=currency_code)
			if currency_code == 'NGN':
				return currency.naira
			elif currency_code == 'USD':
				return currency.usd
			elif currency_code == 'EUR':
				return currency.euro
			elif currency_code == 'GBP':
				return currency.pound
		except Currency.DoesNotExist:
			return None  # Handle missing currency scenario
		return None

	def get_price_in_currency(self, currency_code):
		"""Convert the product price to the selected currency."""
		currency_value = self.get_currency_value(currency_code)
		if currency_value:
			return round(self.price / currency_value, 2)  # Convert and round to 2 decimal places
		return "Conversion Error"

	def get_revised_price(self):
		try:
			jab = Currency.objects.get(pk=1)
			if jab.currency == 'NGN':
				return self.price/jab.naira
			elif jab.currency  == 'USD':
				return self.price/jab.usd
			elif jab.currency == 'EURO':
				return self.price/jab.euro
			elif jab.currency  == 'GBP':
				return self.price/jab.pound
		except Currency.DoesNotExist:
			return None  # Handle missing currency scenario
		return None

	
	def declare_currence(self):
		try:
			jab = Currency.objects.get(pk=1)
			if jab.currency == 'NGN':
				return 'NGN'
			elif jab.currency  == 'USD':
				return 'USD'
			elif jab.currency == 'EURO':
				return 'EURO'
			elif jab.currency  == 'GBP':
				return 'GBP'
		except Currency.DoesNotExist:
			return None  # Handle missing currency scenario
		return None

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address



class Currency(models.Model):
	currecy_choices =[('NGN','Naira'),('GBP','Pound'),('EURO','Euro'),('USD','usd')]
	currency  =  models.CharField((""), max_length=50 ,choices=currecy_choices, default='NGN')
	naira = models.DecimalField((""), max_digits=5, decimal_places=2,default= 1)
	pound =models.DecimalField((""), max_digits=5, decimal_places=2,default= 1)
	euro =models.DecimalField((""), max_digits=5, decimal_places=2,default= 1)
	usd = models.DecimalField((""), max_digits=5, decimal_places=2,default= 1)
	
	
	def __str__(self):
		return self.currency

