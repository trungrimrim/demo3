from django.shortcuts import render,redirect
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def view_list(request):
    """TODO: Docstring for view_list.

    :request: TODO
    :returns: TODO

    """
    items = Item.objects.all()
    return render(request, 'list.html', {'items':items})

def home_page(request):
    """TODO: Docstring for home_page.
    :returns: TODO

    """
    #return HttpResponse('<html><title>Property list</title></html>')
    #if request.method == 'POST':
        #return HttpResponse(request.POST['item_text'])
    #return render(request, 'home.html')

    #item = Item()
    #item.text = request.POST.get('item_text','')
    #item.save()

    #return render(request,'home.html',{
        #'new_item_text': item.text ,
        
        #})

    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list/',{'new_item_text':new_item_text})

    items = Item.objects.all()

    return render(request,'home.html', {'items': items})
