from django.db import models
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your models here.




class Page(models.Model):
    class MenueChoices(models.IntegerChoices):
        MAIN = 0, _("Main"),
        META = 1, _("Meta"),
        NONE = 2, _("None")

    title = models.CharField(max_length=50, verbose_name=_("Title"))
    slug = models.SlugField(max_length=50, unique=True, verbose_name=_("Slug"))
    meta_description = models.CharField(max_length=160, blank=True, null=True, verbose_name=_("Meta description"))
    meta_custom = models.TextField(blank=True, null=True, verbose_name=_("Meta custom tags"))
    #articles = models.ManyToManyField("Article", blank=True)

    # menu = models.PositiveSmallIntegerField(choices=MenueChoices, default=MenueChoices.MAIN)
    # menu_order = models.PositiveIntegerField(default=0)
    url_path = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("URL path"))
    is_reverse = models.BooleanField(default=False, verbose_name=_("Is reverse"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))
    is_home = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))


    def __str__(self):
        return f"#{self.id} {self.title}"
    

    def get_all_pagearticles(self):
        return self.pagearticle_set.all()
    
    def get_published_pagearticles(self):
        return self.get_all_pagearticles().filter(published=True)
    

    def get_absolute_url(self):
        if self.url_path != None:
            if self.is_reverse:
                path = reverse(self.url_path)
            else:
                path = self.url_path

            return path
        if self.is_home:
            return reverse("homepage")
        return reverse("sevo-pages-detail", kwargs={"slug": self.slug})
    

    def is_active(self, path):
        return False
    
    @classmethod
    def get_home_page(cls):
        try:
            home = cls.objects.get(is_home=True)
        except:
            home = False
        return home
    
    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")


class Article(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    title = models.CharField(max_length=150, verbose_name=_("Title"))

    content = models.TextField(verbose_name=_("Content"))
    # order = models.PositiveIntegerField(default=0)
    # page = models.ForeignKey("Page", blank=True, null=True, on_delete=models.SET_NULL)
    published = models.BooleanField(default=True, verbose_name=_("Published"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"#{self.id} {self.title} [{self.name}]"
    

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")




class PageArticle(models.Model):
    page = models.ForeignKey(Page, blank=True, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_("Article"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))

    def __str__(self):
        return f"#{self.id} [Page: #{self.article.id} [name: {self.article.name}, title: {self.article.title}]]"
    

    def get_article(self):
        return self.article
    

    

    class Meta:
        ordering = ["order"]
        verbose_name = _("Page Article")
        verbose_name_plural = _("Page Articles")



class PageMenu(models.Model):
    menu = models.ForeignKey("Menu", blank=True, null=True, on_delete=models.SET_NULL)
    page = models.ForeignKey(Page, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_("Page"))
    url_path = models.SlugField(blank=True, null=True, verbose_name=_("URL path"))
    is_reverse = models.BooleanField(default=False, verbose_name=_("Is reverse"))
    order = models.PositiveIntegerField(default=0, verbose_name=_("Order"))
    published = models.BooleanField(default=True, verbose_name=_("Published"))

    def __str__(self):
        return(f"#{self.id} Page Menu [#{self.page.id} {self.page.title}]")
    
    def get_url_path(self, is_reverse=False):
        from django.urls import reverse
        if is_reverse:
            return reverse(self.url_path)
        return self.url_path
    

    def get_page(self):
        return self.page

    class Meta:
        ordering = ["order"]
        verbose_name = _("Page Menu")
        verbose_name_plural = _("Page Menus")



class Menu(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def get_all_pagemenus(self):
        return self.pagemenu_set.all()
    

    def get_published_pagemenus(self):
        return self.get_all_pagemenus().filter(published=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")
