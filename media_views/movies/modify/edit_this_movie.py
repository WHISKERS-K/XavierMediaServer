import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Movies

   
def edit_this_movie(request:HttpRequest, movie_id):
    sel_movie = Movies.objects.get(id=movie_id)
    
    if request.method == 'POST':
        new_name = request.POST.get('movie_name')
        new_file = request.FILES.get('movie_file')
        curent_name = sel_movie.movie_name 

        ## WE CHANGE THE NAME IF IT ISNT THE SAME
        if curent_name != new_name:
            sel_movie.movie_name = new_name

        ### OPTIONAL WE CHANGE THE FILE
        if new_file:
            #1. we delete the old file.
            old_file_path = sel_movie.movie_file.path

            if os.path.isfile(old_file_path):
                os.remove(old_file_path)

            #2. we asign it the new file
            sel_movie.movie_file = new_file #type: ignore

        sel_movie.save()
        return redirect('show_all_movies')

    ##END POST
    render_template = 'movies/modify/edit_this_movie.html'
    pass_me = {
        'prev_movie_name': sel_movie.movie_name,
    }

    return render(request, render_template, pass_me)