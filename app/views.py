from django.shortcuts import render
from django.http import HttpResponse
from django.template import engines
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    color = request.GET.get('color', 'red')
    return HttpResponse('<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>')



def about(request):
    title = 'App'
    author = 'Délita Makanda'
    html = render_to_string('about.html', {'title': title, 'author': author})

    return HttpResponse(html)
