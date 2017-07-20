from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
# Red pk 1
class Story(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('stories:detailview', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Branch(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    author = None
    creator = None
    content = models.TextField()
    votes = list()

    def __str__(self):
        return self.story + " - " + self.author
