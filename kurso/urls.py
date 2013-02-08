from django.conf.urls import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^kurso/', include('kursoapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += staticfiles_urlpatterns()