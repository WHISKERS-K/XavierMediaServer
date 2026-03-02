from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Movies

# gets the movie id from the url
# then deletes it and redirects to all the movies
def delete_this_movie(request:HttpRequest, movie_id):
    try:
        selected_movie = Movies.objects.get(id=movie_id)
        selected_movie.delete()
        return redirect('show_all_movies')
    except:
        return HttpResponse("EEeeRM, WHAT THE SIGMA???")
    