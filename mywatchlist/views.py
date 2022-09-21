from django.shortcuts import render
from mywatchlist.models import ListFilm
from django.http import HttpResponse
from django.core import serializers
def show_mywatchlist(request):
    list_film = ListFilm.objects.all()
    context = {
        'list_film': list_film,
        'nama': 'Muhammad Rayhan Denel',
        'npm' : '2106752161'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = ListFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ListFilm.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ListFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ListFilm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Create your views here.
