from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "immo_test/index.html",  {
        "title": "Immo test index"
    })