import json
from django.http import HttpResponse
from django.template import loader
from places.models import Place, PlaceImage
from places.views import get_place_json
from django.urls import reverse


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
    template = loader.get_template("index.html")
    context = {"places": places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
