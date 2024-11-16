from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
import os


User = get_user_model()

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Picture(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="immo_m2m/images")
    tags = models.ManyToManyField("Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_inline_title(self):
        return "Klappt"

  

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
    


        
    

class Immo(models.Model):
    title = models.CharField(max_length=255)
    pictures = models.ManyToManyField("Picture", blank=True, related_name="bilder")
    created_at = models.DateTimeField(auto_now_add=True)
    #picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # def delete(self, *args, **kwargs):
    #     print("DEL IMMO")
    #     pics = self.picture_set.all()

    #     for pic in pics:
    #         if os.path.isfile(pic.image.path):
    #             os.remove(pic.image.path)

    #     return super().delete(*args, **kwargs)



class UserPicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    @admin.display(description="Image preview")
    def get_image_tag(self):
        return self.picture.get_image_tag()