import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test

from media.models import Movies
from media_views.utility.check_priv import can_modify, can_view

@user_passes_test(can_view, login_url='homepage')
@user_passes_test(can_modify, login_url='homepage')
def add_this_movie(request:HttpRequest):
    if request.method == 'POST':
        files = request.FILES.getlist('movie_files')

        for file in files:
            #EXTRACT THE NAME FROM THE FILE
            name, extension = os.path.splitext(file.name)

            #IF A MOVIE WITH THE SAME NAME EXISTS IT WILL BE SKIPPED
            already_exists = Movies.objects.filter(movie_name=name).exists()
            if already_exists is True:
                continue

            new_movie = Movies(
                movie_name=name,
                movie_file=file
            )
            
            new_movie.save()
        
        return redirect('show_all_movies')
    
    render_template = 'movies/modify/add_this_movie.html'
    render_args = {
        
    }
    
    return render(request, render_template, render_args)
    
    

