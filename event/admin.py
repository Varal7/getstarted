from django.contrib import admin
from django.contrib.auth.models import *
# Register your models here.

from .models import Participant


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Participant)
