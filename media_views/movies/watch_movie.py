from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from media.models import Movies

# gets the id from the url
# then passes it to the html
def watch_movie(request:HttpRequest, movie_id):
    try:
        movie = Movies.objects.get(id=movie_id)
        render_template = 'movies/watch_movie.html'
        render_args = {
            'movie':movie
        }

        return render(request, render_template, render_args)
    except Movies.DoesNotExist:
        return HttpResponse(f"Movie by id={movie_id} does not exist")
    