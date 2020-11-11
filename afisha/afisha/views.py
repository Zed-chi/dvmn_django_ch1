import json
from django.http import HttpResponse
from django.template import loader
from places.models import Place, PlaceImage



def get_places_dict():
    result = {"type": "FeatureCollection","features": []}
    places = Place.objects.all()
    for place in places:
        detailsUrl = {
            "title": place.title,
            "imgs": [img.image.url for img in place.images.all()],
            "description_short": place.description_short,
            "description_long": place.description_long,
            "coordinates": {
                "lat": place.lat,
                "lng": place.long
            }
        }
        placeInfo = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.long, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": detailsUrl
            }
        }
        result["features"].append(placeInfo)
    return result
    

def index(request):
    places = get_places_dict()
    template = loader.get_template("index.html")
    context = {"places":places}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
