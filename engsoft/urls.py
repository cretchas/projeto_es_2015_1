from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sirius.views.index'),
    url(r'^adiciona_documento/', 'sirius.views.adiciona_documento'),
    url(r'pdf/(?P<id>\d+)/$', 'sirius.views.pdf'),
    # url(r'^engsoft/', include('engsoft.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/fotos/', include('django.contrib.admindocs.urls')),
    url(r'^admin/fotos(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

    #url(r'^view_imagem/', 'sirius.views.view_imagem'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
