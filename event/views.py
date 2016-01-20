from django.shortcuts import render, redirect
from urllib.parse import urlencode
import time
import json
import hashlib

# Create your views here.

FKZ_KEY = "csu"
fields = ['hruid', 'email', 'firstname', 'lastname', 'promo', 'rights']

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

def logout(request):
    for el in fields:
        del request.session[el]
    request.session['authentificated'] = False
    request.session.modified = True
    return redirect("/")

def fkz_answer(request):
    if not "timestamp" in request.GET.keys() or not "response" in request.GET.keys() or not "hash" in request.GET.keys():
        return redirect("/login_required/")
    response = request.GET.get("response")
    ts = request.GET.get("timestamp")
    h = request.GET.get("hash")
    c = (ts + FKZ_KEY + response).encode('utf-8')
    if abs(int(time.time()) - int(ts)) > 600:
        return redirect("/login_required/")

    if hashlib.md5(c).hexdigest() != h:
        return redirect("/login_required/")

    data = json.loads(response)
    for el in fields:
        request.session[el] = data[el]
    print (request.session['lastname'])
    request.session['authentificated'] = True
    return redirect("/")


def fkz_do_login(request):
    ts = str(int(time.time()))
    page = "http://localhost:8000/fkz_answer"
    r = json.dumps(["names", "email", "promo", "rights"])
    c = (ts + page + FKZ_KEY + r).encode('utf-8')
    h = hashlib.md5(c).hexdigest()
    return redirect("http://www.frankiz.net/remote?"+urlencode([('timestamp',ts),('site',page),('hash',h),('request',r)]))
