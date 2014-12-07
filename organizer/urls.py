__author__ = 'connor'
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'^team/(?P<id>\d+)/$',
        'organizer.views.view_team',
        name='view_team'
    ),
)