from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . forms import SignUpForm, SignUpForm2, LoginForm, ChangeUserDataForm, ChangePasswordForm, SetNewPasswordForm, ForgotPasswordForm
from . models import PasswordResetToken



# Create your views here.

# fake home
def fake_home(request):
    return render(request, "sevo_auth/fake_home.html", {
        "title": "Fake home"
    })

# index
def index(request):
    user = request.user
    return render(request, "sevo_auth/index.html", {
        "title": "Auth index",
        "user": user
    })

# def sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()

#             login(request=request, user=user)
#             return redirect("sevo-auth-fake-home")
#     else:
#         form = SignUpForm()
#     return render(request, "sevo_auth/sign_up.html", {
#         "title": "Sign up",
#         "form": form
#     })

# sign up
def sign_up(request):
    form = SignUpForm2()

    if request.method == "POST":
        form = SignUpForm2(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]            

            if password1 == password2:
                try:
                    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
                    user.set_password(password1)
                    user.save()
                    login(request=request, user=user)
                except IntegrityError as e:
                    print(e)

            return redirect("sevo-auth-fake-home")

         
    return render(request, "sevo_auth/sign_up.html", {
        "title": "Sign up",
        "form": form
    })


# sign in
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            print("jjjj")
            print(user.username)
            if user is not None:
                login(request=request, user=user)
                return redirect("sevo-auth-index")
        
    return render(request, "sevo_auth/login.html", {
        "title": "Login",
        "form": form
    })


# sign out
def sign_out(request):
    logout(request)
    return redirect("sevo-auth-index")


# change user data
@login_required(login_url="sevo-auth-sign-in")
def change_user_data(request):
    current_user = request.user

    initial_values = {
        "username": current_user.username,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email,
    }
    form = ChangeUserDataForm(initial=initial_values)

    if request.method == "POST":
        form = ChangeUserDataForm(request.POST, initial=initial_values)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            current_user.username = username
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.email = email

            current_user.save()
                    

    return render(request, "sevo_auth/change_user_data.html", {
        "title": "Change user data",
        "form": form
    })



# change password
@login_required(login_url="sevo-auth-sign-in")
def change_password(request):
    user = request.user

    form = ChangePasswordForm()

    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 == password2:
                user.set_password(password1)
                user.save()
                login(request=request, user=user)
                return redirect("sevo-auth-index")

    return render(request, "sevo_auth/change_password.html", {
        "title": "Change password",
        "form": form
    })


# forgot password
def forgot_password(request):
    form = ForgotPasswordForm()

    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]

            try:
                user = User.objects.get(username=username, email=email)
                print(user)
                prt_exist = False
                try:
                    prt = PasswordResetToken.objects.get(user=user, done=False)
                    prt_exist = True
                except:
                    prt = PasswordResetToken(user=user)
                
                print(prt)
                if not prt_exist:
                    prt.save()
                url = reverse("sevo-auth-set-new-password", args=[prt.token])
                response = HttpResponseRedirect(url)
                domain = request.build_absolute_uri('/')[:-1]
                link = f"{domain}{response.url}"
                print("###############################################")
                print(f"Resetlink per Mail: {link}")
                print("###############################################")
                return redirect("sevo-auth-index")
            except:
                return redirect("sevo-auth-forgot-password")


    return render(request, "sevo_auth/forgot_password.html", {
        "title": "Forgot password",
        "form": form
    })


# set new password
def set_new_password(request, token):
    prt = get_object_or_404(PasswordResetToken, token=token, done=False)
    #prt = PasswordResetToken.objects.get(token=token)
    form = SetNewPasswordForm()

    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            user = prt.user
            if user.username == username and user.email == email and password1 == password2:
                user.set_password(password1)
                user.save()
                prt.done = True
                prt.save()
                login(request=request, user=user)
                return redirect("sevo-auth-index")

            

            

    return render(request, "sevo_auth/set_new_password.html", {
        "title": "New password",
        "form": form
    })


