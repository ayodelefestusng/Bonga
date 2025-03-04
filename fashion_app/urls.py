from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	# path('', views.store, name="store"),
 	path('', views.mainstore, name='mainstore'),

 	path('edit_currency/', views.edit_currency, name='edit_currency'),
 	path('store/<int:pk>/', views.store, name='store'),
  	path('cart/', views.cart, name="cart"),
   	path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('checkout/', views.checkout, name="checkout"),
 
 
 	path('checkout1/', views.payment_checkout, name='checkout_payment'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('payment_failed', views.payment_failed, name='payment_failed'),
 
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
 	path('backoffice/', views.backoffice, name="backoffice"),
   	path('camp/', views.camp, name="camp"),
  	
  
#    path('mainstore1/<int:pk>/', views.mainstore1, name='mainstore1'),
   
     path('yemis/', views.yemis, name='yemis'),
	
 

]