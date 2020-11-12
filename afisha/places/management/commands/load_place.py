import os
import json
import requests
from io import BytesIO
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, PlaceImage
from afisha.settings import BASE_DIR
from requests import HTTPError


class Command(BaseCommand):
    help = "Loading bunch of places"
    LOAD_DIR = os.path.join(BASE_DIR, "load")

    def add_arguments(self, parser):
        parser.add_argument("place_json_url", type=str)

    def get_dict_from_json(self, url):
        res = requests.get(url)
        return json.loads(res.text)

    def handle(self, *args, **options):
        try:
            info = self.get_dict_from_json(options["place_json_url"])
            place, created = Place.objects.get_or_create(
                title=info["title"],
                description_short=info["description_short"],
                description_long=info["description_long"],
                lat=info["coordinates"]["lat"],
                long=info["coordinates"]["lng"],
            )
            place.save()
            img_urls = info["imgs"]
            for order, url in enumerate(img_urls):
                name = url.split("/")[-1]
                image = PlaceImage()
                image.image.save(name, BytesIO(requests.get(url).content), save=False)
                image.order = order + 1
                image.place = place
                image.save()
            self.stdout.write(self.style.SUCCESS("Successfully loaded new places"))
        except (HTTPError, ConnectionError, FileExistsError, CommandError) as e:
            self.stdout.write(self.style.ERROR(e))
