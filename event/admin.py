from django.contrib import admin
from django.contrib.auth.models import *
# Register your models here.

from .models import Participant, Event


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Participant)
admin.site.register(Event)
