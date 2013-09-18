from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'os_project.core.views.home', name='home'),
    url(r'^login/', "django.contrib.auth.views.login", {"template_name": "login.html"}, name='login'),
    url(r'^logout/', "django.contrib.auth.views.logout_then_login", {'login_url': '/login/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^orderservice/(?P<pk>\d+)/$', 'os_project.core.views.orderservice', name='orderservice'),
    
    url(r'^cliente/list/$', 'os_project.core.views.clientes', name='cliente_list'),
    url(r'^cliente/add/$', 'os_project.core.views.cliente', name='cliente_add'),
    url(r'^cliente/edit/(?P<pk>\d+)/$', 'os_project.core.views.cliente', name='cliente_edit'),
    url(r'^cliente/delete/conf/(?P<pk>\d+)/$', 'os_project.core.views.cliente_delete', name='cliente_delconf'),
    url(r'^cliente/delete/(?P<pk>\d+)/$', 'os_project.core.views.cliente_delete', name='cliente_delete'),
)

