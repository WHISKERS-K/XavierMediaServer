from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from media.models import Series, Episodes

def watch_series(request:HttpRequest, series_id, episode_id):
    try:
        series = Series.objects.get(id=series_id)
        episode = Episodes.objects.get(id=episode_id)

        render_template='series/watch_series.html'
        render_args={
            'series':series,
            'episode':episode
        }
        
        return render(request, render_template, render_args)
    except:
        return HttpResponse('error in watch_series')