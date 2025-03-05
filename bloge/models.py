from django.db import models
from django.utils import timezone
from django.utils.text import slugify



class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    slug=models.SlugField(unique=True,max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)                                                                                   

    def __str__(self):
        return self.title
    

class Content(models.Model):
    content=models.TextField()

    def __str__(self):
        return self.content

    

class Hotel(models.Model):
    menu=models.TextField()

    def __str__(self):
        return self.menu