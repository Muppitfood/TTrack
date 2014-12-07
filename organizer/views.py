from django.shortcuts import render_to_response
from organizer.models import Match


# Create your views here.
def index(request):
    return render_to_response('index.html', {
        'matches': Match.objects.all().order_by('id')
    })
