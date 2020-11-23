from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", required=True, unique=True)
    short_description = models.TextField(verbose_name="Короткое описание", blank=True)
    long_description = HTMLField(verbose_name="Детальное описание", blank=True)
    lat = models.FloatField(verbose_name="Широта")
    long = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "title",
        ]
        verbose_name = "Место события"
        verbose_name_plural = "Места событий"


class PlaceImage(models.Model):
    image = models.ImageField(
        upload_to="./images", verbose_name="Файл изображения"
    )
    order = models.IntegerField(default=1, verbose_name="Порядок")
    place = models.ForeignKey(
        "Place",
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Место события",
    )

    def __str__(self):
        return f"{self.order} {self.place.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = "Фото события"
        verbose_name_plural = "Фото событий"
