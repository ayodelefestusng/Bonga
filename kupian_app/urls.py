from django.urls import path

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("register", views.register, name="register"),
    path("load", views.load, name="load"),
    path("redeem", views.redeem, name="redeem"),
        path("result", views.result, name="result"),
         path("add_product", views.add_product, name="add_product"),
          path("create_gift", views.create_gift, name="create_gift"),
          path("winnings", views.winnings, name="winnings"),
          path("yemi", views.yemi, name="yemi"),
    
   path('lookup/', views.value_lookup, name='value_lookup'),

    path("todolist", views.todolist, name="todolist"),
    path("login", auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    # path("logout", auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path('logout', views.user_logout, name ='logout'),
    
    #   path("ggg", views.index, name="index"),
    # # ex: /polls/5/
    #      path("load", views.load, name="load"),
    # # ex: /polls/5/
    # path("<question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
   

]


