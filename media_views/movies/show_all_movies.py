from django.views.generic import ListView

from media.models import Movies

class ShowAllMovies(ListView):
    model = Movies
    template_name = 'movies/show_all_movies.html'
    context_object_name = 'movies'