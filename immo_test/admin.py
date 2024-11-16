from django.contrib import admin

from .models import Picture, Immo

# Register your models here.

# class PictureAdmin(admin.ModelAdmin):
#     list_display = [
#         "title",
#         "get_image_tag",
        
#     ]
#     fields = [
#         "title",
#         "image",
#         "get_link_image_tag",
#         "get_image_url",
#         "created_at",
#         "updated_at",
#     ]

#     readonly_fields = [
#         "created_at",
#         "updated_at",
#         "get_image_tag",
#         "get_link_image_tag",
#         "get_image_url"
#     ]



# class PictureInline(admin.StackedInline):
#     model = Immo.pictures.through
#     extra = 0

#     verbose_name = "Picture"
#     verbose_name_plural = "Pictures"
#     #hide_title = True



# class ImmoAdmin(admin.ModelAdmin):
#     model = Immo
#     inlines = [
#         PictureInline
#     ]

#     exclude = [
#         "pictures"
#     ]



# admin.site.register(Picture, PictureAdmin)

# admin.site.register(Immo, ImmoAdmin)


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 0

    fields = [
        "title",
        "get_image_tag",
        "image",  
    ]

    readonly_fields = [
        "get_image_tag",
    ]

class ImmoAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline
    ]


admin.site.register(Immo, ImmoAdmin)
admin.site.register(Picture)










