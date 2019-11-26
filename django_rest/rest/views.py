from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_home(request):
    return HttpResponse('<h1>Hello world</h1>')
