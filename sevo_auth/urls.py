from django.urls import path

from .views import sign_up, index, sign_in, sign_out, change_user_data, change_password, set_new_password, forgot_password

urlpatterns = [
    path("sign-up/", sign_up, name="sevo-auth-sign-up"),
    path("sign-in/", sign_in, name="sevo-auth-sign-in"),
    path("sign-out/", sign_out, name="sevo-auth-sign-out"),
    path("change-user-data/", change_user_data, name="sevo-auth-change-user-data"),
    path("change-password/", change_password, name="sevo-auth-change-password"),
    path("forgot-password/", forgot_password, name="sevo-auth-forgot-password"),
    path("set-new-password/<str:token>/", set_new_password, name="sevo-auth-set-new-password"),
    path("", index, name="sevo-auth-index")
]
