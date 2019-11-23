# Create your models here.
# first created model
from django.db import models


class Snippet(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()

    class Meta:
        ordering = ['created']
 # now create migrations


def save(self, *args, **kwargs):

    super(Snippet, self).save(*args, **kwargs)
