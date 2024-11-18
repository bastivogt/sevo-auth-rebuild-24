from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     username = forms.CharField(max_length=255, required=True)
#     first_name = forms.CharField(max_length=255, required=True)
#     last_name = forms.CharField(max_length=255, required=True)
#     password1 = forms.CharField(widget=forms.PasswordInput(render_value=True))
#     password2 = forms.CharField(widget=forms.PasswordInput(render_value=True))


#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "email",
#             "first_name",
#             "last_name",
#             "password1",
#             "password2"
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         #print(vars(self))
#         #print(self.fields["password2"])

#         self.fields["email"].label = "Email"
#         self.fields["username"].label = "Username"
#         self.fields["first_name"].label = "Firstname"
#         self.fields["last_name"].label = "Lastname"
#         self.fields["password1"].label = "Password"
#         self.fields["password2"].label = "Password confirm"


#         self.fields["email"].widget.attrs["class"] = "form-control"
#         self.fields["username"].widget.attrs["class"] = "form-control"
#         self.fields["first_name"].widget.attrs["class"] = "form-control"
#         self.fields["last_name"].widget.attrs["class"] = "form-control"
#         self.fields["password1"].widget.attrs["class"] = "form-control"
#         self.fields["password2"].widget.attrs["class"] = "form-control"

# sign up        
class SignUpForm2(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(vars(self))
        #print(self.fields["password2"])

        self.fields["email"].label = _("Email")
        self.fields["username"].label = _("Username")
        self.fields["first_name"].label = _("Firstname")
        self.fields["last_name"].label = _("Lastname")
        self.fields["password1"].label = _("Password")
        self.fields["password2"].label = _("Password confirm")


        for item in self.fields:
            self.fields[item].label_suffix = ""



        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

        
# login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for item in self.fields:
            self.fields[item].label_suffix = ""


        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["class"] = "form-control"



# change user data
class ChangeUserDataForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(vars(self))
        #print(self.fields["password2"])

        self.fields["email"].label = _("Email")
        self.fields["username"].label = _("Username")
        self.fields["first_name"].label = _("Firstname")
        self.fields["last_name"].label = _("Lastname")

        for item in self.fields:
            self.fields[item].label_suffix = ""

        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["first_name"].widget.attrs["class"] = "form-control"
        self.fields["last_name"].widget.attrs["class"] = "form-control"



# change password
class ChangePasswordForm(forms.Form):
    password_old = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(vars(self))
        #print(self.fields["password2"])

        self.fields["password_old"].label = _("Password old")
        self.fields["password1"].label = _("Password new")
        self.fields["password2"].label = _("Password new confirm")


        for item in self.fields:
            self.fields[item].label_suffix = ""

        self.fields["password_old"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"



# set forgot password
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["email"].label = _("Email")
        self.fields["username"].label = _("Username")

        for item in self.fields:
            self.fields[item].label_suffix = ""

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"



# set new password
class SetNewPasswordForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=255, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=True))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=True))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = _("Email")
        self.fields["username"].label = _("Username")
        self.fields["password1"].label = _("Password")
        self.fields["password2"].label = _("Password confirm")

        for item in self.fields:
            self.fields[item].label_suffix = ""


        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"