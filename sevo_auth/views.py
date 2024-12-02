from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext as _
from django.contrib import messages

from django.core.mail import send_mail

from . forms import SignUpForm2, LoginForm, ChangeUserDataForm, ChangePasswordForm, SetNewPasswordForm, ForgotPasswordForm
from . models import PasswordResetToken

from . import settings



# Create your views here.

# fake home
def fake_home(request):
    return render(request, "sevo_auth/fake_home.html", {
        "title": _("Fake home")
    })

# index
def index(request):
    user = request.user
    return render(request, "sevo_auth/index.html", {
        "title": _("Auth index"),
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
    if settings.SEVO_AUTH_CAN_SIGN_UP:
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
                print(username, email, first_name, last_name)        

                if password1 == password2:
                    try:
                        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
                        user.set_password(password1)
                        user.save()
                        login(request=request, user=user)
                        messages.add_message(request, messages.SUCCESS, _("You are sigend up!"))
                    except IntegrityError as e:
                        messages.add_message(request, messages.ERROR, _("Something went wrong!"))
                        print(e)
                        return render(request, "sevo_auth/sign_up.html", {
                            "title": _("Sign up"),
                            "form": form
                        })
                        

                #return redirect("sevo-auth-index")
                return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_SIGN_IN)

            
        return render(request, "sevo_auth/sign_up.html", {
            "title": _("Sign up"),
            "form": form
        })
    else:
        return redirect(settings.SEVO_AUTH_REDIRECT_IF_CANT_SIGN_UP)


# sign in
def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request=request, user=user)
                messages.add_message(request, messages.SUCCESS, _("You are signed in!"))
                return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_SIGN_IN)
            else:
                messages.add_message(request, messages.ERROR, _("You are not signed in!"))
        
    return render(request, "sevo_auth/login.html", {
        "title": _("Login"),
        "form": form
    })


# sign out
@login_required(login_url="sevo-auth-sign-in")
def sign_out(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, _("You are signed out!"))
    return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_SIGN_OUT)


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
            try:
                current_user.save()
                messages.add_message(request, messages.SUCCESS, _("User data changed!"))
                return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_USER_DATA_CHANGE)
            except:
                messages.add_message(request, messages.ERROR, _("Something went wrong! User data not changed!"))
                    

    return render(request, "sevo_auth/change_user_data.html", {
        "title": _("Change user data"),
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
            password_old = form.cleaned_data["password_old"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            # tmp_user = authenticate(request, username=user.username, password=password_old)

            #old_pwd_ok = check_password()

            if user.check_password(password_old):
                if password1 == password2:
                    user.set_password(password1)
                    user.save()
                    login(request=request, user=user)
                    messages.add_message(request, messages.SUCCESS, _("Password changed!"))
                    return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_PASSWORD_CHANGE)
                else:
                    messages.add_message(request, messages.ERROR, _("Something went wrong, try again!"))

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
                send_mail(
                    _("Passwordreset"),
                    f"Resetlink: {link}",
                    #settings.EMAIL_HOST_USER,
                    "auth@django.com",
                    [user.email],
                    fail_silently=False,
                )       
                return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_FORGOT_PASSWORD)
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
                messages.add_message(request, messages.SUCCESS, _("New password setted!"))
                return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_SET_NEW_PASSWORD)
            else:
                messages.add_message(request, messages.ERROR, _("Something went wrong, ty again!"))
            

            

    return render(request, "sevo_auth/set_new_password.html", {
        "title": "New password",
        "form": form
    })




@login_required(login_url="sevo-auth-sign-in")
def delete(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect(settings.SEVO_AUTH_REDIRECT_AFTER_DELETE)
    return render(request, "sevo_auth/delete.html", {
        "title": _("Delete")
    })