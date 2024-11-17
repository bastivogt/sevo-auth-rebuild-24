from django.db import models
from django.utils.translation import gettext as _

# Create your models here.




class Page(models.Model):
    class MenueChoices(models.IntegerChoices):
        MAIN = 0, _("Main"),
        META = 1, _("Meta"),
        NONE = 2, _("None")

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    meta_custom = models.TextField(blank=True, null=True)
    #articles = models.ManyToManyField("Article", blank=True)

    menu = models.PositiveSmallIntegerField(choices=MenueChoices, default=MenueChoices.MAIN)
    menu_order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"#{self.id} {self.title}"
    

    def get_articles(self):
        return self.pagearticle_set.all()
    
    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")


class Article(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)

    content = models.TextField()
    # order = models.PositiveIntegerField(default=0)
    # page = models.ForeignKey("Page", blank=True, null=True, on_delete=models.SET_NULL)
    # published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} {self.title} [{self.name}]"
    

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")




class PageArticle(models.Model):
    page = models.ForeignKey(Page, blank=True, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f"#{self.article.id} [name: {self.article.name}, title: {self.article.title}]"
    

    class Meta:
        ordering = ["order"]
        verbose_name = _("Page Article")
        verbose_name_plural = _("Page Articles")