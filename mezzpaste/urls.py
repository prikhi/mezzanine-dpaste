from django.conf.urls import url, patterns, include
from django.conf import settings

L = getattr(settings, 'DPASTE_SLUG_LENGTH', 4)

urlpatterns = patterns('mezzpaste.views',

    url(r'^$', 'snippet_new', name='snippet_new'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{%d,})/?$' % L, 'snippet_details',
        name='snippet_details'),

    (r'', include('dpaste.urls.dpaste')),
)
