from django.shortcuts import render_to_response, get_object_or_404
from organizer.models import Match, Team, Player


# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'matches': Match.objects.all().order_by('id')
    })


def view_team(request, id):
    team = get_object_or_404(Team, id=id)
    return render_to_response('view_team.html', {
        'team': team,
        'players': Player.objects.filter(team=team)
    })
