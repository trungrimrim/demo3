from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    """TODO: Docstring for home_page.
    :returns: TODO

    """
    #return HttpResponse('<html><title>Property list</title></html>')
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')

    return render(request,'home.html',{
        'new_item_text': request.POST.get('item_text',''),
        
        })
