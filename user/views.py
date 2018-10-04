from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
	if not request.user.is_authenticated:
		return redirect('login')
	else:
		return render(request, 'user/index.html')

def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	context = {'form' : form}
	return render(request, 'registration/register.html', context)

def deconnexion(request):
	logout(request)
	return redirect('index')