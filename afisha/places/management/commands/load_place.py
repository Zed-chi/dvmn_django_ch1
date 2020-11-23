import os
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

    def load_resource_from(url):
        response = requests.get(url)
        if response.status_code >= 300:
            raise HTTPError(f"Bad status code from {url}")
        return response

    def load_image(self, order, url, place):
        try:
            name = url.split("/")[-1]
            image = PlaceImage()
            image_content = self.load_resource_from(url).content
            image.image.save(name, BytesIO(image_content), save=False)
            image.order = order
            image.place = place
            image.save()
            self.stdout.write(self.style.NOTICE(f"Image {name} saved"))
        except (
            HTTPError,
            ConnectionError,
            FileExistsError,
            CommandError,
        ) as e:
            self.stdout.write(self.style.ERROR(e))

    def handle(self, *args, **options):
        try:
            info = self.load_resource_from(options["place_json_url"]).json()
            place, created = Place.objects.get_or_create(
                title=info["title"],
                defaults={
                    "description_short":info["description_short"],
                    "description_long":info["description_long"],
                    "lat":info["coordinates"]["lat"],
                    "long":info["coordinates"]["lng"],
                }        
            )            
            self.stdout.write(self.style.NOTICE(f"Place {place.title} saved"))
            img_urls = info["imgs"]
            for order, url in enumerate(img_urls, start=1):
                self.load_image(order, url, place)
            self.stdout.write(self.style.SUCCESS("Successfully loaded new places"))
        except (
            HTTPError,
            ConnectionError,
            FileExistsError,
            CommandError,
        ) as e:
            self.stdout.write(self.style.ERROR(e))
