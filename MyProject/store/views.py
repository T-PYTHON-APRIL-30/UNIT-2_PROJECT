from django.shortcuts import render
from django.http import HttpRequest, Http404


# Create your views here.
def indexPage(request:HttpRequest):

    return render(request, "store/index.html")