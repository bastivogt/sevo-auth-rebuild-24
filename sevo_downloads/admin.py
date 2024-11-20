from django.contrib import admin

from .models import Download, DownloadFile

# Register your models here.


class DownloadFileInline(admin.StackedInline):
    model = DownloadFile
    extra = 0
    raw_id_fields = [
        "file"
    ]

    fields = [
        "file"
    ]



class DownloadAdmin(admin.ModelAdmin):

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
        "id",
        "title"
    ]

    readonly_fields = [
        "id",
        "created_at",
        "updated_at"
    ]

    inlines = [
        DownloadFileInline
    ]



admin.site.register(Download, DownloadAdmin)