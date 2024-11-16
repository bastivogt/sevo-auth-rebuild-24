from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.forms.models import ModelForm
from django.http import HttpRequest

from django.contrib.auth import get_user_model

User = get_user_model()

from .models import Picture, Immo, Tag, UserPicture

# Register your models here.

class PictureAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "get_image_tag",
        "get_tags_as_str"
        
    ]
    fields = [
        "title",
        "image",
        "get_link_image_tag",
        "get_image_url",
        "tags",
        "created_at",
        "updated_at",
    ]

    readonly_fields = [
        "created_at",
        "updated_at",
        "get_image_tag",
        "get_link_image_tag",
        "get_image_url"
    ]



class PictureInline(admin.StackedInline):
    model = Immo.pictures.through
    extra = 0

    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    #hide_title = True





class ImmoAdmin(admin.ModelAdmin):
    model = Immo
    inlines = [
        PictureInline
    ]

    exclude = [
        "pictures"
    ]




class UserPictureAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "get_image_tag"
    ]

    fields = [
        "user",
        "picture"
        
    ]



    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            current_user = request.user
            if current_user:
                kwargs['initial'] = current_user.pk
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Tag)
admin.site.register(Picture, PictureAdmin)

admin.site.register(Immo, ImmoAdmin)
admin.site.register(UserPicture, UserPictureAdmin)











