from django.shortcuts import render

from django.http import HttpResponse

def view_home(request):
    return HttpResponse("Welcome to By Noveline")
