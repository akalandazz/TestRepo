from django.contrib import admin
from .models import Shifts, Person, MorningShift, MiddayShift, NightShift

# Register your models here.

@admin.register(Shifts)
class ShiftsAdmin(admin.ModelAdmin):
    list_display = ['title', 'morning', 'midday', 'night']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']



@admin.register(MorningShift)
class MorningShiftAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'start_time', 'end_time', 'date']


@admin.register(MiddayShift)
class MiddayShiftAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'start_time', 'end_time', 'date']


@admin.register(NightShift)
class NightShiftAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'start_time', 'end_time', 'date']