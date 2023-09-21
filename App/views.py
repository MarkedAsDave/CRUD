from django.shortcuts import render
from App.models import Item
from django.http import HttpResponseRedirect

# Home 

def home(request):
    all_item = Item.objects.all().order_by('-created_at')
    return render(request, 'home.html', {"items":all_item})

# add item

def add_item(request):
    if request.method == "POST":
        if request.POST.get('item') \
            and request.POST.get('price') \
            and request.POST.get('qty'):
            item = Item()
            item.item = request.POST.get('item')
            item.price = request.POST.get('price')
            item.qty = request.POST.get('qty')
            item.save()
            return HttpResponseRedirect('/')

    else:
            return render(request, 'add.html')

# View item individually

def item(request, item_id):
    item = Item.objects.get(id = item_id)
    if item != None:
        return render(request, "edit.html", {'item':item})

# edit item

def edit_item(request):
    if request.method == "POST":
        item = Item.objects.get(id = request.POST.get('id'))
        if item != None:

            item.item = request.POST.get('item')
            item.price = request.POST.get('price')
            item.qty = request.POST.get('qty')
            item.save()
            return HttpResponseRedirect('/')

# delete item

def delete_item(request, item_id):
    item = Item.objects.get(id = item_id)
    item.delete()
    return HttpResponseRedirect('/')
