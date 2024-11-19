from django.urls import path

from .views import index, detail

urlpatterns = [
    path("", index, name="sevo-pages-index"),
    path("<slug:slug>/", detail, name="sevo-pages-detail")
]
