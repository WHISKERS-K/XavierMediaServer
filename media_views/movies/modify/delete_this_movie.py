import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from media.models import Movies
from media_views.utility.check_priv import can_modify, can_view

# gets the movie id from the url
# then deletes it and redirects to all the movies
@user_passes_test(can_view, login_url='homepage')
@user_passes_test(can_modify, login_url='homepage')
def delete_this_movie(request:HttpRequest, movie_id, cache_buster):
    try:
        selected_movie = Movies.objects.get(id=movie_id)
    except:
        return HttpResponse(f"movie with id {movie_id} does not exist")

    #1. i remove the movie from storage    
    old_movie_file_path = selected_movie.movie_file.path
    if os.path.isfile(old_movie_file_path):
        os.remove(old_movie_file_path)

    #2. i remove the movie from the database
    selected_movie.delete()

    #3. we go back to all movies page
    return redirect('show_all_movies')