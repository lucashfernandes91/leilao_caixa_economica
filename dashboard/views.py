from django.shortcuts import render
from .models import ItemLot

def home(request):
    itens = ItemLot.objects.all()
    return render(request, 'dashboard/index.html', {'itens' : itens})