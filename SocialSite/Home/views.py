from django.shortcuts import render, HttpResponse
import os

# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('static/test.txt')
