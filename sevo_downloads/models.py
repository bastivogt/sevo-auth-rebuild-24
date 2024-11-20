from django.db import models
from django.utils.translation import gettext as _
from django.contrib import admin

from sevo_media.models import File

# Create your models here.

class DownloadFile(models.Model):
    file = models.ForeignKey(File, blank=True, null=True, on_delete=models.CASCADE)
    download = models.ForeignKey("Download", blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.file)
    
    class Meta:
        verbose_name = _("Download File")
        verbose_name_plural = _("Download Files")


class Download(models.Model):
    title = models.CharField(max_length=50)
    published = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    def get_all_downloadfiles(self):
        return self.downloadfile_set.all()
    
    class Meta:
        ordering = [
            "-updated_at"
        ]

        verbose_name = _("Download")
        verbose_name_plural = _("Downloads")
