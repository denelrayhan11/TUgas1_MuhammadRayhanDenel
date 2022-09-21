from django.db import models

class ListFilm(models.Model):
    film_watched = models.TextField()
    film_tittle = models.TextField()
    film_rating = models.TextField()
    film_release_date = models.TextField()
    film_review = models.TextField()
# Create your models here.
