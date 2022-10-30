from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    poster_url = models.URLField()
    genre = models.CharField(max_length=10)
    release_date = models.DateField()
    score = models.FloatField()
    audience = models.CharField(max_length=10)
    movie_plot = models.TextField()
    created_data = models.DateField(auto_now_add=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)