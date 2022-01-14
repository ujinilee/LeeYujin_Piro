from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Review(models.Model):

    movie_title=models.CharField(max_length=100) #영화제목
    release_date=models.IntegerField() #개봉년도
    review_text=models.TextField()#리뷰 
    genre=models.CharField(max_length=100) #장르
    score=models.FloatField() #별점
    director=models.CharField(max_length=100) #감독
    running_time=models.CharField(max_length=100) #러닝타임
    character=models.CharField(max_length=100) #주연

    