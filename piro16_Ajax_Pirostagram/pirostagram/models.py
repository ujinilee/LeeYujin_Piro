from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    substance = models.TextField()
    like = models.IntegerField(default=0)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(null=True)
