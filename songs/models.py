from django.db import models

# Create your models here.
class Songs(models.Model):
    title=models.CharField( max_length=50)
    slug=models.SlugField()
    body=models.TextField()
    singer=models.CharField( max_length=50)
    thumb=models.ImageField(default='default.jpg',blank=True)
    #add thumbnail

    def __str__(self):
        return self.title

    def snip(self):
        return self.body[:20]+'...'
