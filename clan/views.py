from django.shortcuts import render

# Create your views here.
def clan_list(request):
	return render(request, 'clan_list.html')