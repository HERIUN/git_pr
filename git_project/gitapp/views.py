from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return HttpResponse('hi')

def kdg(request):
    return HttpResponse('kdg')
# Create your views here.
