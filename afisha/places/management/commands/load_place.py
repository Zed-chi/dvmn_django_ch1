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
        image_name = url.split("/")[-1]
        image_content = self.load_resource_from(url).content

        image = PlaceImage.objects.create(order=order, place=place)
        image.image.save(image_name, BytesIO(image_content), save=False)
        self.stdout.write(self.style.NOTICE(f"Image {image_name} saved"))

    def handle(self, *args, **options):
        place_details_json = self.load_resource_from(
            options["place_json_url"]
        ).json()
        place, created = Place.objects.get_or_create(
            title=place_details_json["title"],
            defaults={
                "description_short": place_details_json["description_short"],
                "description_long": place_details_json["description_long"],
                "lat": place_details_json["coordinates"]["lat"],
                "long": place_details_json["coordinates"]["lng"],
            },
        )
        self.stdout.write(self.style.NOTICE(f"Place {place.title} saved"))
        img_urls = place_details_json["imgs"]
        for order, url in enumerate(img_urls, start=1):
            try:
                self.load_image(order, url, place)
            except (
                requests.HTTPError,
                FileExistsError,
            ) as e:
                self.stdout.write(self.style.ERROR(e))

        self.stdout.write(self.style.SUCCESS("Successfully loaded new places"))
