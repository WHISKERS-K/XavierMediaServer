import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Movies

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
    
    

