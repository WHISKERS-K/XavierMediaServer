from django.http import HttpRequest
from django.shortcuts import render

def test_page(request: HttpRequest):
    
    pass_to = {

    }
    return render(request, "learning/first_script.html", pass_to)