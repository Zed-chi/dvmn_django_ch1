from django.db import models
import uuid


# Create your models here.
class Place(models.Model):
    title = models.TextField()
    placeId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    detailsUrl = models.URLField(max_length=250)

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.title