from django.db import models

class Album(models.Model):
    image = models.FilePathField(path="/img")
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    released = models.CharField(max_length=50, null=True)
    description =models.TextField(null=True, blank=True)

