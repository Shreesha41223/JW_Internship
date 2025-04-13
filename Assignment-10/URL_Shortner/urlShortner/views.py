from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Url
import uuid

# Create your views here.
def index(request):
    return render(request, 'index.html')

def shorten_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print(url)  # Debugging line to check the URL received
        if Url.objects.filter(link=url).exists():
            short_url = Url.objects.get(link=url).short_link  # Retrieve existing short link
        else:
            short_url = str(uuid.uuid4())[:5]
            new_url = Url(link=url, short_link=short_url)
            new_url.save()
        content = {
            'short_url': short_url,
        }
        return render(request, 'index.html', content)
    return redirect('index')  # Redirect to index if not a POST request

def redirect_url(request, short_link):
    try:
        url = Url.objects.get(short_link=short_link)
        return redirect(url.link)  # Redirect to the original URL
    except Url.DoesNotExist:
        return render(request, 'index.html', {'error': 'URL not found'})  # Handle error if short link does not exist