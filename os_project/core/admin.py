# coding: utf-8
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import *

class Os_OsItemInline(admin.TabularInline):
    model = OrdemServico.items.through


class OrdemServicoAdmin(admin.ModelAdmin):
    inlines = [
        Os_OsItemInline,
    ]

    def response_add(self, request, obj, post_url_continue="/"):
        return HttpResponseRedirect(reverse("home"))

    def response_change(self, request, obj):
        return HttpResponseRedirect(reverse("home"))

class OrdemServicoItemAdmin(admin.ModelAdmin):
     pass

#class MembroInline(admin.TabularInline):
#     model = Membro
#     exclude = ('tipo',)

# class EquipeAdmin(admin.ModelAdmin):
#     inlines = [MembroInline,]
#
# class ClienteAdmin(admin.ModelAdmin):
#     exclude = ('tipo',)
#
# class PessoaAdmin(admin.ModelAdmin):
#     pass
#
admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(OrdemServicoItem, OrdemServicoItemAdmin)

# admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Pessoa, PessoaAdmin)
# admin.site.register(Equipe, EquipeAdmin)

