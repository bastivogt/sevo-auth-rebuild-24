from django import template
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from sevo_pages.models import Page, Article

from sevo_media.models import Picture, File



register = template.Library()

@register.simple_tag
def is_active_page(path, page):
    # print("path:", path)
    # print("page.title: ", page.title)
    # print("page.get_absolute_url: ", page.get_absolute_url())
    # print(page.get_absolute_url() == path)
    if page.get_absolute_url() == path:
        return "active"
    


# tags for db content
@register.simple_tag
def greeting(name="John"):
    return f"Hello, {name}!"


@register.simple_tag
def get_article_by_id(id):
    try:
        article = Article.objects.get(id=int(id), published=True)
        return render_to_string("sevo_pages/partials/page_tags/_article.html", {
            "article": article
        })
    except:
        return render_to_string("sevo_templatetags/partials/_error.html", {
            "message": "<Article not found>"
        })
    

@register.simple_tag
def image_tag(id, w="400", h="auto", wrapper=True):
    try:
        picture = Picture.objects.get(id=int(id))
        print("Picture Tag", picture)
        return render_to_string("sevo_templatetags/partials/_image.html", {
            "picture": picture,
            "width": w,
            "height": h,
            "wrapper": wrapper
        })
    except:
        return render_to_string("sevo_templatetags/partials/_error.html", {
            "message": "<Picture not found>"
        })
    

@register.simple_tag
def audio_tag(id, download=True, caption=True, download_caption="Download"):
    try:
        audio = File.objects.get(id=int(id))

        return render_to_string("sevo_templatetags/partials/_audio.html", {
            "audio": audio,
            "download": download,
            "download_caption": download_caption,
            "caption": caption
        })
    except:
        return render_to_string("sevo_templatetags/partials/_error.html", {
            "message": "<Audio not found>"
        })
