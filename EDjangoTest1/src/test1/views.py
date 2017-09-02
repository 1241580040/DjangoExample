from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    #request.GET
    #request.POST
    return HttpResponse("Hello World!")

def noindex(request):
    #request.GET
    #request.POST
    return HttpResponse("Hello no World!")


