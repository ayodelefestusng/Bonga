from django.urls import path
from .views import register, password_reset_confirm, password_setup_sent

urlpatterns = [
    path("register/", register, name="register"),
    path("password-setup-sent/", password_setup_sent, name="password_setup_sent"),
    path("password-reset-confirm/<uidb64>/<token>/", password_reset_confirm, name="password_reset_confirm"),
]
