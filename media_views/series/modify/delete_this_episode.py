from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Series, Episodes

def delete_this_episode(request:HttpRequest, series_id, episode_id):
    try:
        series = Series.objects.get(id=series_id)
        episode = Episodes.objects.get(id=episode_id)
        
        episode.delete()

        return redirect('show_series', series_id=series.id) # type: ignore
    except:
        return HttpResponse("error in delete_this_episode")