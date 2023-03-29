from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    HttpResponse("hello world")