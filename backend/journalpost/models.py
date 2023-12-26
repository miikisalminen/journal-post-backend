from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=50, null=True) 
    title = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=20, null=True)
    published = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, null=True)
    origin_url = models.CharField(max_length=500, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title