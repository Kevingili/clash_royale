from django.shortcuts import render
from clan.models import Clan
from user.models import MyUser
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required


class ClanForm(ModelForm):
	class Meta:
		model = Clan
		widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'placeholder':'Description du clan'}),
        }
		#fields = ['name', 'url', 'description', 'users']
		fields = "__all__" 

# Create your views here.
def clan_list(request):
	clans = Clan.objects.all()
	return render(request, 'clan_list.html', {'clans': clans})

def show_clan(request, id_clan):
	clan = Clan.objects.get(id=id_clan)
	if request.POST:
		if request.POST.get("actionF") == "rejoindre":
			user = request.user
			user.clan_id = clan.id
			user.save()
		else:
			user = request.user
			user.clan_id = None
			user.save()
			clans = Clan.objects.all()
			return render(request, 'clan_list.html', {'clans': clans})
	players = MyUser.objects.filter(clan_id=clan.id)
	user = request.user
	if user.clan_id == clan.id:
		test = True
	else:
		test = False
	return render(request, 'show_clan.html', {'players': players, 'clan': clan, 'test': test})

@login_required
def create_clan(request):
	user = request.user
	if user.clan_id != None :
		clans = Clan.objects.all()
		return render(request, 'clan_list.html', {'clans': clans})
	elif request.POST:
			form = ClanForm(request.POST)
			if form.is_valid():
				form.save()
				clans = Clan.objects.all()
				last_clan = Clan.objects.last()
				user.clan_id = last_clan.id
				user.save()
				return render(request, 'clan_list.html', {'clans': clans})
	else:
		form = ClanForm()
	
	return render(request, 'clan_create.html', {'form': form})
