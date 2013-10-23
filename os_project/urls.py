from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'os_project.core.views.home', name='home'),
    url(r'^login/', "django.contrib.auth.views.login", {"template_name": "login.html"}, name='login'),
    url(r'^logout/', "django.contrib.auth.views.logout_then_login", {'login_url': '/login/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^orderservice/list/$', 'os_project.core.views.orderservices', name='orderservice_list'),
    url(r'^orderservice/(?P<pk>\d+)/$', 'os_project.core.views.orderservice', name='orderservice'),

    url(r'^service/list/$', 'os_project.core.views.services', name='service_list'),
    url(r'^service/add/$', 'os_project.core.views.service', name='service_add'),
    url(r'^service/edit/(?P<pk>\d+)/$', 'os_project.core.views.service', name='service_edit'),
    url(r'^service/delete/conf/(?P<pk>\d+)/$', 'os_project.core.views.service_delete', name='service_delconf'),
    url(r'^service/delete/(?P<pk>\d+)/$', 'os_project.core.views.service_delete', name='service_delete'),
    
    url(r'^cliente/list/$', 'os_project.core.views.clientes', name='cliente_list'),
    url(r'^cliente/add/$', 'os_project.core.views.cliente', name='cliente_add'),
    url(r'^cliente/edit/(?P<pk>\d+)/$', 'os_project.core.views.cliente', name='cliente_edit'),
    url(r'^cliente/delete/conf/(?P<pk>\d+)/$', 'os_project.core.views.cliente_delete', name='cliente_delconf'),
    url(r'^cliente/delete/(?P<pk>\d+)/$', 'os_project.core.views.cliente_delete', name='cliente_delete'),

    url(r'^equipe/list/$', 'os_project.core.views.equipes', name='equipe_list'),
    url(r'^equipe/add/$', 'os_project.core.views.equipe', name='equipe_add'),
    url(r'^equipe/edit/(?P<pk>\d+)/$', 'os_project.core.views.equipe', name='equipe_edit'),
    url(r'^equipe/delete/conf/(?P<pk>\d+)/$', 'os_project.core.views.equipe_delete', name='equipe_delconf'),
    url(r'^equipe/delete/(?P<pk>\d+)/$', 'os_project.core.views.equipe_delete', name='equipe_delete'),

    url(r'^membro/list/$', 'os_project.core.views.membros', name='membro_list'),
    url(r'^membro/add/$', 'os_project.core.views.membro', name='membro_add'),
    url(r'^membro/add_equipe/$', 'os_project.core.views.membro_add_equipe', name='membro_add_equipe'),
    url(r'^membro/save_equipe/$', 'os_project.core.views.membro_save_equipe', name='membro_save_equipe'),

    url(r'^membro/edit/(?P<pk>\d+)/$', 'os_project.core.views.membro', name='membro_edit'),
    url(r'^membro/delete/conf/(?P<pk>\d+)/$', 'os_project.core.views.membro_delete', name='membro_delconf'),
    url(r'^membro/delete/(?P<pk>\d+)/$', 'os_project.core.views.membro_delete', name='membro_delete'),
    
)

