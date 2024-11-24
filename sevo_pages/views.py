from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Template, Engine, Context


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
    #content = Template("{% load page_tags %}<h1>{% greeting name='Sevo' %}</h1>")
    #content = Engine.from_string("<h1>Content</h1>")

    #content = Template("{% include 'sevo_pages/partials/_content.html' %}")
    c = ""
    for particle in page.get_published_pagearticles():
        c += f"<h2>{particle.get_article().title}</h2>"
        c += particle.get_article().content
    content = Template("{% load page_tags %}" + f"{c}")
    context = Context({
        "page": page
        })

  


    return render(request, "sevo_pages/detail.html", {
        "page": page,
        "content": content.render(context)
    })
