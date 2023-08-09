from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This is HOMEPAGE")

def about(request):
    return HttpResponse("This is About page")
