from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from cms.sitemaps import CMSSitemap

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
	url(r'^zinnia/', include('zinnia.urls', namespace='zinnia')),
	url(r'^comments/', include('django_comments.urls')),
	url(r'^', include('cms.urls')),
	url(r'^', include('cms.urls', namespace='imagestore')),
	#url(r'^zinnia/', include('zinnia.urls', namespace='zinnia')),
	#url(r'^comments/', include('django_comments.urls')),
	#url(r'^gallery/', include('imagestore.urls', namespace='imagestore')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + staticfiles_urlpatterns() + urlpatterns
