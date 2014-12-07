__author__ = 'connor'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'^team/(?P<id>\d+)/$',
        'organizer.views.view_team',
        name='view_team'
    ),
    url(
        r'^player/(?P<id>\d+)/$',
        'organizer.views.view_player',
        name='view_player'
    ),
    url(
        r'^tournament/(?P<id>\d+)/$',
        'organizer.views.view_tournament',
        name='view_tournament'
    ),
)
