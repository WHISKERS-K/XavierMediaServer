from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from media.models import Episodes, Series

# from django.views.generic import CreateView
# class EpisodeCreateView(CreateView):
#     model = Episodes
#     fields = ['series', 'episode_name', 'episode_file']
#     success_url = 'all_series'

#     template_name = 'modify/create_episode.html'

def add_this_episode(request:HttpRequest, series_id):
    if request.method == 'POST':
        name = request.POST.get('episode_name')
        file = request.FILES.get('episode_file')

        series = Series.objects.get(id=series_id)
        new_episode = Episodes(
            series_fk=series,
            episode_name=name,
            episode_file=file
        )
        new_episode.save()
        return redirect('show_series', series_id=series_id)    
    
    render_template = 'series/modify/add_this_episode.html'
    render_args = {
        
    }
    return render(request, render_template, render_args)