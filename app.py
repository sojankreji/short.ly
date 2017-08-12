from django.conf.urls import url
from django.http import HttpResponse

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uq)b=evycs1+=*3!f0c%3h%(j@_=h%c+=i6363mntz5z)_)k*0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = __name__

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/Users/delitamakanda/Projets/short.ly/templates/',
        ],
    },
]

def home(request):
    color = request.GET.get('color', 'red')
    return HttpResponse('<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>')

from django.template import engines
from django.template.loader import render_to_string

def about(request):
    title = 'App'
    author = 'Délita Makanda'
    html = render_to_string('about.html', {'title': title, 'author': author})

    return HttpResponse(html)

urlpatterns = [
    url(r'^$', home, name="homepage"),
    url(r'^about/$', about, name="aboutpage"),
]
