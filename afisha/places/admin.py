from django.contrib.admin.options import TabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Place, PlaceImage

# Register your models here.
class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ("preview",)
    extra = 0

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

    class Meta:
        ordering = [
            "order",
        ]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]

    class Meta:
        ordering = [
            "order",
        ]


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
