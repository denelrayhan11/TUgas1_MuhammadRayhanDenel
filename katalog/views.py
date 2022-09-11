from django.shortcuts import render
from katalog.models import CatalogItem
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_barang_katalog,
        'nama': 'Muhammad Rayhan Denel',
        'npm' : '2106752161'
    }
    return render(request, "katalog.html", context)
# TODO: Create your views here.
