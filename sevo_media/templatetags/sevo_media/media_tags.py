from django import template
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

from sevo_pages.models import Page, Article


register = template.Library()



@register.simple_tag
def get_article_by_id(id):
    try:
        article = Article.objects.get(id=int(id), published=True)
        return render_to_string("sevo_pages/partials/page_tags/_article.html", {
            "article": article
        })
    except:
        return render_to_string("sevo_pages/partials/page_tags/_error.html", {
            "message": "<Object not found!>"
        })
