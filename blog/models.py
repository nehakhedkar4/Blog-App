from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model): 

    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)
    blog_user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.blog_user.username
    
class UndoPost(models.Model):
    undo_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.username
    


