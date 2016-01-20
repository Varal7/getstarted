from django.shortcuts import render, redirect
from urllib.parse import urlencode
from django.conf import settings
import time
import json
import hashlib
from .forms import *

# Create your views here.


fields = ['hruid', 'email', 'firstname', 'lastname', 'promo', 'rights']

def index(request):
    return render(request, "event/index.html", {'template':True})

def info(request):
    return render(request, "event/info.html")

def contact(request):
    return render(request, "event/contact.html")

def register(request):
    if 'authentificated' in request.session.keys():
        if request.method == "POST":
            try:
                form = RegisterForm(request.POST)
                if form.is_valid():
                    new_user = Participant.objects.create(**form.cleaned_data)
            # redirect, or however you want to get to the main view
                    return HttpResponseRedirect(reverse("register_done"))
            except:
                pass
        else:
            form = RegisterForm(initial={'username': request.session['hruid'],
                                          'first_name': request.session['firstname'],
                                          'last_name': request.session['lastname'],
                                          'email': request.session['email'],
                                          'promo': request.session['promo'],
                                })
        return render(request, "event/register.html", {'form':form})

    else:
        return fkz_do_login(request,"/register")



def register_done(request):
    return render(request, "event/register_done.html")


def logout(request):
    for el in fields:
        del request.session[el]
    del request.session['authentificated']
    request.session.modified = True
    return redirect("/")

def login_required(request):
    return render(request, "event/login_required.html")

def fkz_answer(request):
    if not "timestamp" in request.GET.keys() or not "response" in request.GET.keys() or not "hash" in request.GET.keys():
        return redirect("/login_required/")
    response = request.GET.get("response")
    ts = request.GET.get("timestamp")
    h = request.GET.get("hash")
    location = request.GET.get("location")
    c = (ts + settings.FKZ_KEY + response).encode('utf-8')
    if abs(int(time.time()) - int(ts)) > 600:
        return redirect("/login_required/")

    if hashlib.md5(c).hexdigest() != h:
        return redirect("/login_required/")

    data = json.loads(response)
    for el in fields:
        request.session[el] = data[el]
    print (request.session['lastname'])
    request.session['authentificated'] = True
    return redirect(location)


def fkz_do_login(request, location = "/"):
    ts = str(int(time.time()))
    settings.FKZ_PAGE = "http://localhost:8000/fkz_answer"
    r = json.dumps(["names", "email", "promo", "rights"])
    c = (ts + page + FKZ_KEY + r).encode('utf-8')
    h = hashlib.md5(c).hexdigest()
    return redirect("http://www.frankiz.net/remote?"+urlencode([('timestamp',ts),('site',page),('location',location),('hash',h),('request',r)]))
