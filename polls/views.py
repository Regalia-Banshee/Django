from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Abhi maja ayega na bhidu hehe.")
