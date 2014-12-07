from django.shortcuts import render_to_response, get_object_or_404
from organizer.models import Tournament, Match, Team, Player, Sponsor, Manager


# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'matches': Match.objects.all().order_by('id'),
        'sponsors': Sponsor.objects.all().order_by('id'),
        'managers': Manager.objects.all().order_by('id')
    })


def view_team(request, id):
    team = get_object_or_404(Team, id=id)
    return render_to_response('view_team.html', {
        'team': team,
        'players': Player.objects.filter(team=team)
    })


def view_player(request, id):
    return render_to_response('view_player.html', {
        'player': get_object_or_404(Player, id=id)
    })


def view_tournament(request, id):
    return render_to_response('view_tournament.html', {
        'tournament': get_object_or_404(Tournament, id=id)
    })