from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Place, PlaceImage

# Register your models here.
class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = ("preview",)


    def preview(self, obj):
        return format_html(
            mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.image.url,
                    width="auto",
                    height=200,
                )
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    readonly_fields = ("preview",)

    def preview(self, obj):
        return format_html(
            mark_safe(
                '<img src="{url}" width="{width}" height={height} />'.format(
                    url=obj.image.url,
                    width="auto",
                    height=200,
                )
            )
        )
