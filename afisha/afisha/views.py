from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def get_places_dict():
    result = {"type": "FeatureCollection", "features": []}
    places = Place.objects.all()
    for place in places:
        detailsUrl = reverse("place", kwargs={"place_id": place.id})
        placeInfo = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.long, place.lat],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": detailsUrl,
            },
        }
        result["features"].append(placeInfo)
    return result


def index(request):
    places = get_places_dict()
    return render(request, "index.html", context={"places": places})
