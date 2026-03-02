from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class Series(Model):
    series_name = models.CharField(max_length=128, unique=True, 
                                   null=True, blank=True)
    def __str__(self):
        return self.series_name

class Episodes(Model):
    series_fk = models.ForeignKey(
        Series, 
        on_delete=models.CASCADE,
        related_name='episodes_set'
    )
    
    episode_name = models.CharField(max_length=128, null=True, blank=True)
    episode_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.episode_name


class Movies(Model):
    movie_name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    movie_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.movie_name

class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class FavoritesM(Model):
    user_fk = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    movie_fk = models.ForeignKey(
        Movies,
        on_delete=models.CASCADE
    )

class FavoritesS(Model):
    user_fk = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    series_fk = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
    )

class FavoritesE(Model):
    user_fk = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    episode_fk = models.ForeignKey(
        Series,
        on_delete=models.CASCADE,
    )

