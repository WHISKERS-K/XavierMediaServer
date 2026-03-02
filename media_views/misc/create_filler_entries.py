from media.models import Series
from media.models import SeriesEpisodes
from media.models import Movies

from django.shortcuts import render

def create_filler_entries(request):
    ##SERIES
    fma = Series.objects.create(series_name='Fullmetal Alchemist: Brotherhood')
    jjba = Series.objects.create(series_name="JoJo's Bizarre Adventure")
    arc = Series.objects.create(series_name="Arcane")

    ##SERIES EIPSODES
    for i in range(64):
        e = SeriesEpisodes.objects.create(series=fma, episode_name=f'Episode {i+1}')

    for i in range(190):
        e = SeriesEpisodes.objects.create(series=jjba, episode_name=f'Episode {i+1}')

    for i in range(18):
        e = SeriesEpisodes.objects.create(series=arc, episode_name=f'Episode {i+1}')

    ##MOVIES
    matrix = Movies.objects.create(movie_name='Matrix')
    matrix2 = Movies.objects.create(movie_name='Matrix 2')
    matrix3 = Movies.objects.create(movie_name='Matrix 3')

    return render(request, "tmp_create_filler.html")