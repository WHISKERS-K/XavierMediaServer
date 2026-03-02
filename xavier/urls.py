from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 
from django.conf import settings

#media views
import media.views as mv

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    
    #HOMEPAGE
    path("", mv.homepage, name='homepage'),

    #MOVIES
    path('show_all_movies/', mv.ShowAllMovies.as_view(), name='show_all_movies'),
    path('watch_movie/<movie_id>/', mv.watch_movie, name='watch_movie'),
    path('stream_movie/<movie_id>', mv.stream_movie, name='stream_movie'),
    #MOVIES-MODIFY
    path('add_this_movie/', mv.add_this_movie, name='add_this_movie'),
    path('delete_this_movie/<movie_id>/', mv.delete_this_movie, name='delete_this_movie'),
    path('edit_this_movie/<movie_id>/', mv.edit_this_movie, name='edit_this_movie'),

    #SERIES
    path('show_all_series/', mv.ShowAllSeries.as_view(), name='show_all_series'),
    path('show_series/<series_id>', mv.show_series, name='show_series'),
    path('watch_series/<series_id>/<episode_id>/', mv.watch_series, name='watch_series'),
    #SERIES-MODIFY
    path('add_this_series/', mv.add_this_series, name='add_this_series'),
    path('delete_this_series/<series_id>/', mv.delete_this_series, name='delete_this_series'),
    path('add_this_episode/<series_id>/', mv.add_this_episode, name='add_this_episode'),
    path('delete_this_episode/<series_id>/<episode_id>/', mv.delete_this_episode, name='delete_this_episode'),

    #REGISTER
    path('register/', mv.register_view, name='register'),
    #LOGIN/LOGOUT
    path('login/', mv.login_view, name='login'),
    path('logout/', mv.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
