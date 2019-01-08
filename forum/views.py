from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from forum.models import Topic
from forum.models import Comment
from django import forms

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		widgets = {
		  'description': forms.Textarea(attrs={'rows':4, 'placeholder':'Description du topic'}),
		}
		#fields = ['title', 'description']
		fields = "__all__"

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		labels = {
            "content": "Votre réponse"
        }
		widgets = {
		  'content': forms.Textarea(attrs={'rows':2, 'placeholder':'Répondre...'}),
		}
		#fields = ['title', 'description']
		fields = "__all__"

# Create your views here.
@login_required
def forum_index(request):
	topics = Topic.objects.all()
	return render(request, 'forum_index.html', {'topics': topics})

@login_required
def forum_create(request):
	if request.POST:
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('forum_index')
	else:
		form = TopicForm()
		form.fields["user"].initial = [request.user.id]
	
	return render(request, 'forum_create.html', {'form': form})

@login_required
def forum_show(request, id_forum):
	topic = Topic.objects.get(id=id_forum)
	comments = Comment.objects.all().filter(topic_id=topic.id)
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			#return redirect('forum_show', topic.id)
	else:
		form = CommentForm()
		form.fields["user"].initial = [request.user.id]
		form.fields["topic"].initial = topic
	return render(request, 'forum_show.html', {'topic': topic, 'form': form, 'comments':comments})
