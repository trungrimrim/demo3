from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    """TODO: Docstring for home_page.
    :returns: TODO

    """
    #return HttpResponse('<html><title>Property list</title></html>')
    return render(request, 'home.html')
