from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Movies

def add_this_movie(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('movie_name')
        file = request.FILES.get('movie_file')

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
    
    

