from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to our restaurant reservation system.")
