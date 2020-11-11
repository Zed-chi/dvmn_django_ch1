import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from places.models import Place, PlaceImage

# Create your views here.
def get_place_view(req, id):
    place = get_object_or_404(Place, pk=id)
    return HttpResponse(place.title)
