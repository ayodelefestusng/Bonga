from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
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



def store2(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	# category_id = int(request.POST['your_field'])
	# Com = Category.objects.get(id=category_id)
	# products = Product.objects.filter(category=Com)
	categories=Category.objects.all()
	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems,'categories':categories}
	# products = Product.objects.all()
	# context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store1.html', context)


def camp (request):
    return render(request,'store/fake.html')

def category_list(request):
    products = Product.objects.all()
    categories=Category.objects.all()
    context ={'categories':categories,'products':products}
    return render(request, "store/store-main.html", context)

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
	
 
def edit_currency(request):
    category_id = request.POST['currency']
    cont= Currency.objects.get(pk=1)
    print ('ups')
    cont.currency=category_id
    cont.save()
    return redirect('mainstore') 
  
def mainstore(request):
    currency = Currency.objects.all()
    categories=Category.objects.all()
    products = Product.objects.all()
    items=OrderItem.objects.all()
    cartTotalItems = sum([item.quantity for item in items])
    context = {'products':products, 'categories':categories,'currency':currency,'cartTotalItems':cartTotalItems,'items':items}
    return render(request, 'store/mainstore.html', context)
	# return redirect('store1')


def cart (request):
    products = Product.objects.all()
    order = Order.objects.all()
    items=OrderItem.objects.all()
    cartTotalItems = sum([item.quantity for item in items])
    # OrderItemTotal = sum([item.get_total_product_price for item in items])
    OrderItemTotal = sum([item.get_total_product_price for item in items])
    context ={'order': order,'products': products,'items':items,'cartTotalItems':cartTotalItems,'OrderItemTotal':OrderItemTotal}
    return render(request, 'store/cart.html', context)



def store(request,pk):
	Com = Category.objects.get(id=pk)
	products = Product.objects.filter(category=Com)
	categories=Category.objects.all()
	# products = Product.objects.all()
	items=OrderItem.objects.all()
	cartTotalItems = sum([item.quantity for item in items])
	context = {'products':products,'categories':categories,'cartTotalItems':cartTotalItems}
	return render(request, 'store/mainstore1.html', context)
	# return redirect('mainstore')




def add_to_cart(request, product_id):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    
    order, created = Order.objects.get_or_create(session_key=session_key, completed=False)
    product = get_object_or_404(Product, id=product_id)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    if not created:
        order_item.quantity += 1
    order_item.save()
    # return JsonResponse({'message': 'Item added to cart'})
    return redirect('mainstore')

# def cart(request):
# 	data = cartData(request)
# 	cartItems = data['cartItems']
# 	order = data['order']
# 	items = data['items']

# 	context = {'items':items, 'order':order, 'cartItems':cartItems}
# 	return render(request, 'store/cart.html', context)

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
		# return redirect('store')
		return render(request, 'store/backoffice.html')


	else:
		category_form= CategoryForm()
		product_form =ProductForm()
		currency_form = CurrencyForm()
		context ={'category_form':category_form,'product_form':product_form,'currency_form':currency_form}
		return render(request, 'store/backoffice.html', context)



def yemis(request):
    return render(request, "store/yemi.html")


# views.py

import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET,
})

def create_payment(request):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": { "payment_method": "paypal", },
        "redirect_urls": {"return_url": request.build_absolute_uri(reverse('execute_payment')),
        "cancel_url": request.build_absolute_uri(reverse('payment_failed')),},
        "transactions": [{ "amount": {"total": "10.00",  # Total amount in USD
                    "currency": "USD", }, "description": "Payment for Product/Service", } ],})

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'payment_failed.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment_success.html')
    else:
        return render(request, 'payment_failed.html')

def payment_checkout(request):
    return render(request, 'checkout.html')

def payment_failed(request):
    return render(request, 'payment_failed.html')