from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "event/index.html")

def programm(request):
    return render(request, "event/programm.html")

def news(request):
    return render(request, "event/news.html")

def info(request):
    return render(request, "event/info.html")

def contact(request):
    return render(request, "event/contact.html")
