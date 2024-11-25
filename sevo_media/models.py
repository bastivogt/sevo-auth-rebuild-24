from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext as _

# Create your models here.

class PictureTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-updated_at"
        ]
        verbose_name = _("Picture Tag")
        verbose_name_plural = _("Picture Tags")


class Picture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/images")
    tags = models.ManyToManyField(PictureTag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title} [{self.get_tags_as_str()}]"


    
    def delete(self, *args, **kwargs):
        print("DELETE PICTURE")
        self.image.delete()
  
        return super().delete(*args, **kwargs)
    
    @admin.display(description="Image preview")
    def get_image_tag(self):
        img_tag = f'<img src="{self.image.url}" alt="{self.title}" title="{self.title}" style="width: 80px; height: 80px; object-fit: cover;" />'
        return format_html(img_tag)
    
    @admin.display(description="Image preview link")
    def get_link_image_tag(self):
        a_tag = f'<a href="{self.image.url}" title="{self.title}">{self.get_image_tag()}</a>'
        return format_html(a_tag)
    
    @admin.display(description="Image URL")
    def get_image_url(self):
        if self.image:
            return self.image.url
        return None
    
    
    @admin.display(description="Tags")
    def get_tags_as_str(self):
        tags = self.tags.all()
        tag_list = [item.title for item in tags]
        return ", ".join(tag_list)
    
    class Meta:
        ordering = [
            "-updated_at"
        ]

        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")





class FileTag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-updated_at"
        ]
        verbose_name = _("File Tag")
        verbose_name_plural = _("File Tags")



class File(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to="uploads/files")
    tags = models.ManyToManyField(FileTag, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.get_tags_as_str()}]"
    
    def delete(self, *args, **kwargs):
        print("DELETE File")
        self.file.delete()
  
        return super().delete(*args, **kwargs)

    @admin.display(description="File URL")
    def get_file_url(self):
        if self.file:
            return self.file.url
        return None
    
    @admin.display(description="Tags")
    def get_tags_as_str(self):
        tags = self.tags.all()
        tag_list = [item.title for item in tags]
        return ", ".join(tag_list)
    
    class Meta:
        ordering = [
            "-updated_at"
        ]

        verbose_name = _("File")
        verbose_name_plural = _("Files")


