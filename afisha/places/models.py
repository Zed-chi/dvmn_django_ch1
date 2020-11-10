from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()    
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    image = models.ImageField(upload_to="./images")
    order = models.IntegerField(default=1)
    place = models.ForeignKey("Place", related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order} {self.place.title}"
    
    class Meta:
        ordering = ["order"]