from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    # path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout', views.user_logout, name ='logout'),
     path('logout', views.user_logout, name ='logout'),
     path('admin', views.admin, name ='admin'),
     path('category', views.category, name ='category'),
      path('brand', views.brand, name ='brand'),
    path('product', views.product, name ='product'),
    path('model', views.model, name ='model'),
   path('customer', views.customer, name ='customer'),
    path('invoice', views.invoice, name ='invoice'),
    path('dailyops', views.dailyops, name ='dailyops'),
       path('inventory', views.inventory, name ='inventory'),
        path('transaction', views.transaction, name ='transaction'),
         path('delete/<username>', views.del_user, name ='del_user'),
       
      
    
    # path('create-product/', views.create_product_view, name='create-product'),
    #  path('transaction/', views.transaction, name='transaction'),
    
    # path('agobat/', views.agobat, name='agobat'),

    # path('createBrand/', views.createBrand, name='createBrand'),
    # path('inventory/', views.car_inventory_list, name='car_inventory_list'),
    # path('create/', views.car_inventory_create, name='car_inventory_create'),
    # path('update/<int:pk>/', views.car_inventory_update, name='car_inventory_update'),
    # path('delete/<int:pk>/', views.car_inventory_delete, name='car_inventory_delete'),
    
]

 