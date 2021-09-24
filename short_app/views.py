from django.shortcuts import render, redirect
from .forms import Url
from django.contrib.auth.decorators import login_required
from .models import UrlData



@login_required
def index(request):
    if request.method == "POST":
        tut = Url(request.POST)
        if tut.is_valid():
            url = tut.cleaned_data["url"]
            slug = tut.cleaned_data['slug']
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            return redirect('links')
    else:
        tut = Url()


    return render(
        request,
        'short_app/links.html', 
        {
            'tut': tut,
            'news': UrlData.objects.all()
            }
        )

def urlRedirect(request, url):
    data = UrlData.objects.get(url=url)
    return redirect(data.url)

