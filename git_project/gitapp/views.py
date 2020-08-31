from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hi')

def ws(request):
    return HttpResponse("WOOSEOP")
# Create your views here.
