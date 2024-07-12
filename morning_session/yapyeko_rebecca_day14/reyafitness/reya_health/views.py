from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def content(request):
    return HttpResponse('<h1>Welcome to ReyaFitness!<h1>')