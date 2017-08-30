from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MiniUrl
from .forms import MiniUrlForm
from django.contrib import messages

# Create your views here.
def about(request):
    title = 'App'
    author = 'Délita Makanda'

    return render(request, 'about.html', {'title': title, 'author': author})


def liste(request):
    minis_list = MiniUrl.objects.order_by('-nb_acces')
    page = request.GET.get('page', 1)
    max_count = minis_list.count()
    title = 'Short.ly'

    paginator = Paginator(minis_list, 10)
    try:
        minis = paginator.page(page)
    except PageNotAnInteger:
        minis = paginator.page(1)
    except EmptyPage:
        minis = paginator.page(paginator.num_pages)

    return render(request, 'index.html', locals()) #built-in function for avoid writing variables in context


#def success_miniurl(request, pk):
    #mini = get_object_or_404(MiniUrl, pk=pk)
    #return render(request, 'success.html', {'mini': mini})


def nouveau(request):
    if request.method == 'POST':
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            mini = form.save(commit=False)
            mini.date = timezone.now()
            form.save()
            messages.success(request, mini.url + ' was shortened.')
            return redirect('liste')
    else:
        form = MiniUrlForm()
    return render(request, 'nouveau.html', {'form' : form})

def redirection(request, code):
    mini = get_object_or_404(MiniUrl, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)
