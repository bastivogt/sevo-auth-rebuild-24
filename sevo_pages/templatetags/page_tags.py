from django import template
from django.http import HttpResponseRedirect

from sevo_pages.models import Page


register = template.Library()

@register.simple_tag
def is_active_page(path, page):
    # print("path:", path)
    # print("page.title: ", page.title)
    # print("page.get_absolute_url: ", page.get_absolute_url())
    # print(page.get_absolute_url() == path)
    if page.get_absolute_url() == path:
        return "active"
    



@register.simple_tag
def greeting(name="John"):
    return f"Hello, {name}!"
