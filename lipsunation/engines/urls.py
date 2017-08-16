from django.conf.urls import url, include

from lipsunation.engines.views import (
    index,
    detail,
    lorem_ipsum
)


urlpatterns = [
    # ex: /engines/
    url(r'^$', index, name='index'),
    # ex: /engines/5/
    url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/lorem_ipsum/(?P<paragraph_count>[0-9]+)$', lorem_ipsum, name='lorem_ipsum'),

    # ex: /engines/5/generate
    # url(r'^(?P<engine_id>[0-9]+)/generate/(?P<paragraph_count>[0-9]+)?$', generate, name='generate'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
