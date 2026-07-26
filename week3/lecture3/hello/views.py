from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")


def aadesh(request):
    return render(request, "hello/index.html")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()})