from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

User = get_user_model()

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_unusable_password()  # Ensure the user must set a password
            user.save()
            send_password_setup_email(user, request)
            return redirect("password_setup_sent")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

def send_password_setup_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    password_reset_link = request.build_absolute_uri(
        reverse("password_reset_confirm", kwargs={"uidb64": uid, "token": token})
    )

    subject = "Set Up Your Password"
    message = render_to_string("password_setup_email.html", {"link": password_reset_link})

    send_mail(subject, message, "your-email@gmail.com", [user.email])

def password_setup_sent(request):
    return render(request, "password_setup_sent.html")





from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse

def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(User, pk=uid)
    except Exception:
        return HttpResponse("Invalid link", status=400)

    if not default_token_generator.check_token(user, token):
        return HttpResponse("Invalid token", status=400)

    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SetPasswordForm(user)

    return render(request, "password_reset_confirm.html", {"form": form})





# SEND EMAIL

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


def send_email(request):
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email", "")
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ["admin@example.com"])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect("/contact/thanks/")
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")