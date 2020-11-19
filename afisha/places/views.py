import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from places.models import Place


def get_place_json(req, id):
    place = get_object_or_404(Place, pk=id)
    detailsUrl = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {"lat": place.lat, "lng": place.long},
    }
    return JsonResponse(
        detailsUrl, safe=False, json_dumps_params={"ensure_ascii": False}
    )
