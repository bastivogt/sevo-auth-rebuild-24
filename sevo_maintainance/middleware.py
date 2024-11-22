from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .settings import SEVO_MAINTAINANCE


class SevoMaintainanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # before view
        print("SMM", request.user)
        print("SMM", request.path)
        if SEVO_MAINTAINANCE:
            if not "admin" in request.path and not request.user.is_superuser and not request.path == reverse("sevo-maintainance"):
                #return HttpResponse("SEVO MAINTAINANCE")
                # return render(request, "sevo_maintainance/maintainance.html", {
                #     "title": "Maintainance Mode"
                # })
                return redirect("sevo-maintainance")

        #return HttpResponse("SEVO MAINTAINANCE")
        response = self.get_response(request)
        # after view

        return response