from unicodedata import category
from django.db import models

# Create your models here.

class Devtool(models.Model):
    #이름, 종류, 개발툴 설명
    dev_name=models.CharField(max_length=100) ##
    dev_type=models.CharField(max_length=100)
    dev_content=models.TextField()

    def __str__(self):
        return self.dev_name


#, choices=TOOL_CHOICES

class Idea(models.Model):
    #아이디어명, 대표사진, 아이디어 설명, 아이디어 관심도, 예상개발툴(리스트)
    idea_name=models.CharField(max_length=200)
    idea_image=models.ImageField(upload_to='swidea',blank=True,null=True)
    idea_content=models.TextField()
    idea_like=models.IntegerField(default=0)
    devtool=models.ForeignKey(Devtool, on_delete=models.CASCADE) ##

    def __str__(self):
        return self.idea_name


