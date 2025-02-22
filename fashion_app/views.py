from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)



def category1(request):
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
		
def backoffice(request):
	if request.method =="POST":
		category_load = CategoryForm(request.POST or None)
		if category_load.is_valid ():
			category_load.save()
		product_load = ProductForm(request.POST or None)
		if product_load.is_valid ():
			product_load.save()
		currency_load = CurrencyForm(request.POST or None)
		if currency_load.is_valid ():
			currency_load.save()
		messages.success(request,("Category Succesful Created, Kindly Login "))
		return redirect('store')

	else:
		category_form= CategoryForm()
		product_form =ProductForm()
		currency_form = CurrencyForm()
		context ={'category_form':category_form,'product_form':product_form,'currency_form':currency_form}
		return render(request, 'store/backoffice.html', context)