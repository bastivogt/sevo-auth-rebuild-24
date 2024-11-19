from django.contrib import admin
from django.utils.translation import gettext as _

from .models import Page, Article, PageArticle, PageMenu, Menu

# class ArticleInline(admin.StackedInline):
#     model = Article
#     raw_id_fields = ["page"]
#     extra = 0



class PageArticleInline(admin.StackedInline):
    model = PageArticle
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "name",
        "created_at",
        "updated_at",
        "published"
    ]

    list_display_links = [
        "id",
        "title"
    ]

    list_filter = [
        "created_at",
        "updated_at",
        "published"
    ]

    search_fields = [
        "title",
        "content"
    ]




class PageAdmin(admin.ModelAdmin):
    raw_id_fields = [
        "picture"
    ]
    fields = [
        "title",
        "slug",
        "meta_description",
        "meta_custom",
        "picture",
        "url_path",
        "is_reverse",
        "published",
        "is_home"
    ]
    list_display = [
        "id",
        "title",
        # "menu",
        # "menu_order",
        "get_image_tag",
        "created_at",
        "updated_at",
        "is_home",
        "published",
    ]

    list_display_links = [
        "id",
        "title",
        "get_image_tag"
    
    ]

    prepopulated_fields = {
        "slug": ("title", )
    }

    inlines = [
        PageArticleInline
    ]

    # exclude = [
    #     "articles"
    # ]
    


class PageMenuInline(admin.StackedInline):
    model = PageMenu
    extra = 0

    fieldsets = [
        (None, {
            "fields": [
                "page", 
                "order",
                "published"
            ]
        }),
        (_("Advanced"), {
            "classes": ["wide, collapse"],
            "fields": [
                "url_path",
                "is_reverse"
            ]
        })
    ]

class MenuAdmin(admin.ModelAdmin):
    inlines = [
        PageMenuInline
    ]

    list_display = [
        "name",
        "get_published_pages_str",
        "get_all_pages_str"
    ]


#admin.site.register(PageMenu)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
