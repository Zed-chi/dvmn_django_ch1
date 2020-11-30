import os
from io import BytesIO

import requests
from afisha.settings import BASE_DIR
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Loading bunch of places"
    LOAD_DIR = os.path.join(BASE_DIR, "load")

    def add_arguments(self, parser):
        parser.add_argument("place_json_url", type=str)

    def load_resource_from(self, url):
        response = requests.get(url)
        response.raise_for_status()        
        return response

    def load_image(self, order, url, place):
        try:
            name = url.split("/")[-1]            
            image_content = self.load_resource_from(url).content

            image = PlaceImage.objects.create(
                order=order, place=place
            )
            image.image.save(name, BytesIO(image_content), save=False)            
            self.stdout.write(self.style.NOTICE(f"Image {name} saved"))
        except (
            requests.HTTPError,
            FileExistsError,
        ) as e:
            self.stdout.write(self.style.ERROR(e))

    def handle(self, *args, **options):
        info = self.load_resource_from(options["place_json_url"]).json()
        place, created = Place.objects.get_or_create(
            title=info["title"],
            defaults={
                "description_short": info["description_short"],
                "description_long": info["description_long"],
                "lat": info["coordinates"]["lat"],
                "long": info["coordinates"]["lng"],
            },
        )
        self.stdout.write(self.style.NOTICE(f"Place {place.title} saved"))
        img_urls = info["imgs"]
        for order, url in enumerate(img_urls, start=1):
            self.load_image(order, url, place)
        self.stdout.write(self.style.SUCCESS("Successfully loaded new places"))
