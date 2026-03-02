from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from media.models import Series, Episodes

def show_series(request:HttpRequest, series_id):
    try:
        series = Series.objects.get(id=series_id)
        episodes = Episodes.objects.filter(series_fk=series)

        render_template='series/show_series.html'
        renger_args={
            'series':series,
            'episodes':episodes
        }

        return render(request, render_template, renger_args)
    except Series.DoesNotExist:
        return HttpResponse(f"Series by id={series_id} does not exist")
    