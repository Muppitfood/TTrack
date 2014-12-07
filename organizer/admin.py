from django.contrib import admin
from organizer.models import *

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    pass


class TournamentAdmin(admin.ModelAdmin):
    pass


class MatchAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


class ManagerAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location, LocationAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Sponsor, SponsorAdmin)