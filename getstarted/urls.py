"""getstarted URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from event import views


urlpatterns = [
    url(r'^admin', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^register$', views.register, name='register'),
    url(r'^update$', views.update_cv, name='update_cv'),
    url(r'^register_done$', views.register_done, name='register_done'),
    url(r'^fkz_answer$', views.fkz_answer, name='fkz_answer'),
    url(r'^login$', views.fkz_do_login, name='login'),
    url(r'^login_required$', views.login_required, name='login_required'),
    url(r'^logout$', views.logout, name='logout'),


    url(r'^', views.index, name='index'),
]
