from django.contrib import admin

from .models import Gallery, GalleryPicture
from sevo_media.models import Picture

# Register your models here.



class GalleryPictureInline(admin.StackedInline):
    model = GalleryPicture
    extra = 0
    raw_id_fields = [
        "picture"
    ]

    fields = [
        "picture",
        "get_image_tag"
    ]

    readonly_fields = [
        "get_image_tag"
    ]



class GalleryAdmin(admin.ModelAdmin):

    fields = [
        "id",
        "title",
        "published"
    ]

    list_display = [
        "id",
        "title",
        "created_at",
        "updated_at",
        "published"
    ]

    list_display_links = [
        "title"
    ]

    readonly_fields = [
        "id",
        "created_at",
        "updated_at"
    ]

    inlines = [
        GalleryPictureInline
    ]

    raw_id_fields = [
        "pictures"
    ]


admin.site.register(Gallery, GalleryAdmin)