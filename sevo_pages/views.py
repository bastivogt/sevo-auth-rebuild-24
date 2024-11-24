from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Template, Engine, Context
from django.template.loader import get_template


from .models import Page

# Create your views here.

def index(request):
    return HttpResponse("Pages index")



def homepage(request):
    page = get_object_or_404(Page, is_home=True)
    
    return render(request, "sevo_pages/detail.html", {
        "page": page
    })

def detail(request, slug):
    page = get_object_or_404(Page, slug=slug)

    print("path: ", request.path)


  


    return render(request, "sevo_pages/detail.html", {
        "page": page,
    })
