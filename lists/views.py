from django.shortcuts import render,redirect
from django.http import HttpResponse

from lists.models import Item,List

# Create your views here.
def add_item(request, list_id):
    """TODO: Docstring for add_item.

    :request: TODO
    :returns: TODO

    """
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/'%(list_.id))

def new_list(request):
    """TODO: Docstring for new_list.

    :request: TODO
    :returns: TODO

    """
    #item = Item()
    #item.text = request.POST['item_text']
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list =list_)
    return redirect('/lists/%d/'%(list_.id))

def view_list(request, list_id):
    """TODO: Docstring for view_list.

    :request: TODO
    :returns: TODO

    """
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.all()
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list':list_})

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

    #if request.method == 'POST':
        #new_item_text = request.POST['item_text']
        #Item.objects.create(text=new_item_text)
        #return redirect('/lists/the-only-list/',{'new_item_text':new_item_text})

    #items = Item.objects.all()

    return render(request,'home.html')
