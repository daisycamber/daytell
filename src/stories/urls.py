from django.conf.urls import url
from . import views

app_name = 'stories'

urlpatterns = [
    #/stories/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/stories/<story_id>/
    url(r'^(?P<story_id>[0-9]+)/$', views.detailview, name='detailview'),

    #/stories/<story_id>/branch/ - Add new branch to story
    url(r'^(?P<story_id>[0-9]+)/branch/$', views.create_branch, name='create_branch'),

    #/stories/story/add/
    url(r'story/add/$', views.create_story, name='story-add'),

    #/stories/story/2/delete
    url(r'^(?P<story_id>[0-9]+)/delete/$', views.StoryDelete.as_view(), name='story-delete'),
]
