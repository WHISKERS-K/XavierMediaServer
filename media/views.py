from django.shortcuts import render


## MOVIES
from media_views.movies.show_all_movies import ShowAllMovies
from media_views.movies.watch_movie import watch_movie
## MOVIES-MODIFY
from media_views.movies.modify.add_this_movie import add_this_movie
from media_views.movies.modify.delete_this_movie import delete_this_movie

## SERIES
from media_views.series.show_all_series import ShowAllSeries
from media_views.series.show_series import show_series
from media_views.series.watch_series import watch_series
## SERIES-MODIFY
from media_views.series.modify.add_this_series import add_this_series
from media_views.series.modify.delete_this_series import delete_this_series
from media_views.series.modify.add_this_episode import add_this_episode
from media_views.series.modify.delete_this_episode import delete_this_episode

## REGISTER
from media_forms.accounts.register import register_view

## LOGIN / LOGOUT
from media_forms.accounts.login import login_view
from media_forms.accounts.login import logout_view

##STREAMING
from media_views.video.stream_movie import stream_movie

##LEARNING
from media_views.test.first_script import test_page

# # CreateView
# class EpisodeCreateView(CreateView):
#     model = SeriesEpisodes
#     fields = ['series', 'episode_name', 'episode_file']
#     success_url = 'all_series'

#     template_name = 'modify/create_episode.html'

def homepage(request):
    return render(request, 'homepage.html')