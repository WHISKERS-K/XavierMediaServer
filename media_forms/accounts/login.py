from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            ##checks if the password/username are correct and
            ##returns a user if so
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                return redirect('login')
    else:
        form = AuthenticationForm()
    
    render_template='account/actions/login.html'
    render_args = {
        'form': form
    }
    return render(request, render_template, render_args)

def logout_view(request):
    logout(request)
    return redirect("homepage")