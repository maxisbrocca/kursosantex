from django.conf.urls import patterns, url
from views import home, new
from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
    url(r'^home/$', home, name='home_view'),
    url(r'^new/(?P<classname>.+)$', new, name='new'),
    url(r'^ingresar/$', auth_views.login, {'template_name': 'ingresar.html'},
        name='ingresar'),
    url(r'^salir/$', auth_views.logout,  {'template_name': 'salir.html'},
        name='salir'),
    )
