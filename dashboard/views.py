from django.shortcuts import render
from .models import ItemLot as ListItems

def home(request):
    items = ListItems.objects.all()
    return render(request, 'dashboard/index.html', {'list_items' : items})

def list_items(request):
    items = ListItems.objects.all()
    return render(request, 'dashboard/list_items.html', {'list_items': items})