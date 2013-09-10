# coding: utf-8
from django.contrib import admin
from models import *

class MembroInline(admin.TabularInline):
    model = Membro

class EquipeAdmin(admin.ModelAdmin):
    inlines = [
        MembroInline,
    ]

admin.site.register(Membro)
admin.site.register(Equipe, EquipeAdmin)