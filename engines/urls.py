from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /engines/
    url(r'^$', views.index, name='index'),
    # ex: /engines/5/
    url(r'^(?P<engine_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(generate$', views.generate, name='generate'),
    
    # ex: /engines/5/generate
    url(r'^(?P<engine_id>[0-9]+)/generate/(?P<paragraph_count>[0-9]+)?$', views.generate, name='generate'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]