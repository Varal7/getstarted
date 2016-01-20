from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from urllib.parse import urlencode
from django.conf import settings
import time
import json
import hashlib
from .forms import *
from .models import Participant


# Create your views here.


fields = ['hruid', 'email', 'firstname', 'lastname', 'promo', 'rights']

def index(request):
    return render(request, "event/index.html", {'template':True})

def info(request):
    return render(request, "event/info.html")

def contact(request):
    return render(request, "event/contact.html")

def isRegistered(hruid):
    return Participant.objects.filter(username=hruid, isActive=True).exists()


def register(request):
    if 'authentificated' in request.session.keys():
        if request.method == "POST":
            form = RegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # redirect, or however you want to get to the main view
                request.session['registered'] = True
                return redirect(reverse('index') + '#register_done')

        else:
            if isRegistered(request.session['hruid']):
                return redirect(reverse('index') + '#already_registered')
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

    request.session['authentificated'] = True
    if isRegistered(request.session['hruid']):
        request.session['registered'] = True
    else:
        request.session['registered'] = False
    return redirect(location)

def fkz_do_login(request, location = "/"):
    ts = str(int(time.time()))
    r = json.dumps(["names", "email", "promo", "rights"])
    c = (ts + settings.FKZ_PAGE + settings.FKZ_KEY + r).encode('utf-8')
    h = hashlib.md5(c).hexdigest()
    return redirect("http://www.frankiz.net/remote?"+urlencode([('timestamp',ts),('site',settings.FKZ_PAGE),('location',location),('hash',h),('request',r)]))
