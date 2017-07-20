from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import BranchForm, StoryForm
from .models import Story, Branch

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'stories/index.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        return Story.objects.all()

def detailview(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'stories/detail.html', {'story':story})

def create_story(request):
    form = StoryForm(request.POST or None)
    if form.is_valid():
        story = form.save(commit=False)
        story.save()
        return render(request, 'stories/detail.html', {'story':story})
    return render(request, 'stories/story_form.html',{'form':form})

def create_branch(request, story_id):
    if request.user.is_authenticated():
        form = BranchForm(request.POST or None)
        story = get_object_or_404(Story, pk=story_id)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.creator = request.user
            print(branch.creator)
            branch.story = story
            branch.save()

            return render(request, 'stories/detail.html', {'story':story})
        return render(request, 'stories/detail.html', {'story':story, 'form':form})
    return render(request, 'stories/detail.html', {'story':get_object_or_404(Story, pk=story_id)})

class StoryDelete(DeleteView):
    model = Story
    success_url = reverse_lazy('stories:index')
