from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from user.models import MyUser
from django.contrib.auth.decorators import login_required
from .forms import MyCustomUserForm

def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		return render(request, 'user/index.html')

def register(request):

	if request.method == 'POST':
		form = MyCustomUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = MyCustomUserForm()
	context = {'form' : form}
	return render(request, 'registration/register.html', context)

def deconnexion(request):
	logout(request)
	return redirect('index')

@login_required
def user_list(request):
	users = MyUser.objects.all()
	return render(request, 'user/user_list.html', {'users': users})

@login_required
def show_player(request, id_user):
	player = MyUser.objects.get(id=id_user)
	cards = player.card_set.all()
	return render(request, 'user/show_player.html', {'player': player, 'cards': cards})

@login_required
def my_account(request):
	u1 = request.user
	return render(request, 'user/my_account.html')
