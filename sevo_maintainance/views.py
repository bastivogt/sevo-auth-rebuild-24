from django.shortcuts import render, redirect
from .settings import SEVO_MAINTAINANCE

# Create your views here.


def maintainance(request):
    if not SEVO_MAINTAINANCE:
        return redirect("homepage")
    return render(request, "sevo_maintainance/maintainance.html", {
        "title": "Maintainance Mode"
    })