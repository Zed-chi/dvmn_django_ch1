from django.contrib import admin
from .models import Place, PlaceImage

# Register your models here.
class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


#admin.site.register(Place)
admin.site.register(PlaceImage)