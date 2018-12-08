from django.shortcuts import render
from clan.models import Clan
from user.models import MyUser

# Create your views here.
def clan_list(request):
	clans = Clan.objects.all()
	return render(request, 'clan_list.html', {'clans': clans})

def show_clan(request, id_clan):
	clan = Clan.objects.get(id=id_clan)
	players = MyUser.objects.filter(clan_id=clan.id)
	return render(request, 'show_clan.html', {'players': players, 'clan': clan})