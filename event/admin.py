from django.contrib import admin
from django.contrib.auth.models import *
# Register your models here.

from .models import Participant, Event, Startup


admin.site.unregister(User)
admin.site.unregister(Group)

class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'is_active', 'hits')
    readonly_fields = ('hits','name')

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_joined',  'email',  'cv')
    fields = ('first_name', 'last_name', 'date_joined',  'email',  'cv', 'year_in_school', 'promo', 'found_stage', 'domains', 'missions', 'want_cocktail', 'is_active')
    readonly_fields = ('first_name', 'last_name', 'date_joined',  'email', 'promo', 'cv', 'promo', 'year_in_school', 'found_stage', 'domains', 'missions', 'want_cocktail')


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Startup)
