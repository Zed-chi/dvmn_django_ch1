from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Place


def get_place_json(req, place_id):
    place = get_object_or_404(Place, pk=place_id)
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
