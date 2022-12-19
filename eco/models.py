from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class EcoPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='download.jpg', upload_to='image')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])