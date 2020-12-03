from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = [
        "preview",
    ]
    extra = 0

    def preview(self, obj):        
        if obj.image:
            return format_html(
                '<img src="{src}" width="{width}" height={height} />',
                src=obj.image.url,
                width="auto",
                height=200,
            )
        return "Изображение еще не загружено"
        
    class Meta:
        ordering = [
            "order",
        ]


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        PlaceImageInline,
    ]
    search_fields = [
        "title",
    ]

    class Meta:
        ordering = [
            "order",
        ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(PlaceImageAdmin, self).get_queryset(request)
        qs = qs.select_related("place")
        return qs

    readonly_fields = [
        "preview",
    ]

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{src}" width="{width}" height={height} />',
                src=obj.image.url,
                width="auto",
                height=200,
            )
        return "Изображение еще не загружено"
