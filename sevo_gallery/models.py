from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin

from sevo_media.models import Picture


# Create your models here.

class GalleryPicture(models.Model):
    picture = models.ForeignKey(Picture, blank=True, null=True, on_delete=models.CASCADE)
    gallery = models.ForeignKey("Gallery", blank=True, null=True, on_delete=models.CASCADE)

    @admin.display(description="Picture Preview")
    def get_image_tag(self):
        return self.picture.get_image_tag()
    
    def __str__(self):
        return str(self.picture)
    
    class Meta:
        verbose_name = _("Gallery Picture")
        verbose_name_plural = _("Gallery Pictures")


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    pictures = models.ManyToManyField(Picture, blank=True, related_name="bilder")
    gallery_pictures = models.ManyToManyField(GalleryPicture, blank=True, related_name="galeriebilder")
    published = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    def get_all_gallerypictures(self):
        return self.gallerypicture_set.all()
    
    class Meta:
        ordering = [
            "-updated_at"
        ]

        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")