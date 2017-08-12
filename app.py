from django.conf.urls import url
from django.http import HttpResponse

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uq)b=evycs1+=*3!f0c%3h%(j@_=h%c+=i6363mntz5z)_)k*0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = __name__

def home(request):
    color = request.GET.get('color', 'red')
    return HttpResponse('<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>')

def about(request):
    title = 'App'
    author = 'Délita Makanda'
    html = '''<!DOCTYPE html>
    <html>
    <head>
      <title>''' + title + '''</title>
    </head>
    <body>
        <h1>About ''' + title + '''</h1>
        <p>This Website was developed by ''' + author + '''.</p>
    </body>
    </html>'''
    return HttpResponse(html)

urlpatterns = [
    url(r'^$', home),
    url(r'^about/$', about),
]
