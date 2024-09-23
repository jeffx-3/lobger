from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=28)
    slug = models.SlugField(default='')
    photo = models.ImageField(upload_to='images/')
    author =models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                      related_name='article')
    body = models.TextField(max_length=6000, default='')
    published =models.DateTimeField(default=timezone.now)
    
    class Meta:
     ordering = ['-published']
     indexes =[
     models.Index(fields=['-published']),
     ]
   
    def __str__(self):
     return self.title
 
    def get_absolute_url(self):
      return "/blogs/{self.slug}/"