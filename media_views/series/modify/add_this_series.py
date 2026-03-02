from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Series

def add_this_series(request:HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('series_name')

        new_series = Series(series_name=name)
        new_series.save()
        return redirect('show_all_series')
    
    render_template = 'series/modify/add_this_series.html'
    render_args = {
        
    }
    return render(request, render_template, render_args)

    
    

