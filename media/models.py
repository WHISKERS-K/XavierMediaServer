import os
import uuid

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

def movies_files_by_id(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"

    return f"movies/{new_filename}"

class Movies(Model):
    movie_name = models.CharField(max_length=128, unique=True, null=True, blank=True)
    movie_file = models.FileField(null=True, blank=True, upload_to=movies_files_by_id)

    def __str__(self):
        return self.movie_name

#>0 = viewing permission
#>1 = modifying permission
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    priv = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self) -> str:
        return self.user.get_username()

