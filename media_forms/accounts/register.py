from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from media.models import Profile

def register_view(request:HttpRequest):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #SAVES THE USER MODEL

            Profile.objects.create(
                user=user
            )

            return redirect('homepage')
    else:
        form = UserCreationForm()

    render_template='account/actions/register.html'
    render_args = {
        'form': form
    }
        
    return render(request, render_template, render_args)