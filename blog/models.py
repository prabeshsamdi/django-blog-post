from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    titleImage = models.ImageField(upload_to='images/', blank=True, null=True)
    
    # Add default values for new fields
    first = models.TextField(default='')
    firstImage = models.ImageField(upload_to='images/', blank=True, null=True)
    second = models.TextField(default='')
    secondImage = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class About(models.Model):
    full_name =models.CharField(max_length=200, unique=False)
    about =models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to='images/',blank=True,null=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.full_name