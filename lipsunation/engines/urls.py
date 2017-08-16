from django.conf.urls import url, include

from lipsunation.engines.views import (
    ListView,
    DetailView,
    LoremIpsumView
)

urlpatterns = [
    url(r'^$', ListView, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', DetailView, name='detail'),
    url(r'^(?P<slug>[\w-]+)/lorem_ipsum/(?P<paragraph_count>[0-9]+)$', LoremIpsumView, name='lorem_ipsum'),
]
