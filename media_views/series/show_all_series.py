from django.views.generic import ListView

from media.models import Series

class ShowAllSeries(ListView):
    model = Series
    template_name = 'series/show_all_series.html'
    context_object_name = 'series'