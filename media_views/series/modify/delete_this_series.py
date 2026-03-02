from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from media.models import Series

def delete_this_series(request:HttpRequest, series_id):
    try:
        series = Series.objects.get(id=series_id)
        series.delete()
        
        return redirect('all_series')
    except:
        return HttpResponse("EEeeRM, WHAT THE SIGMA???")