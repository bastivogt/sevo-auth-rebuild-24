from django.contrib import admin

from .models import Page, Article, PageArticle

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
    ]

    list_display_links = [
        "id",
        "title"
    ]

    list_filter = [
        "created_at",
        "updated_at"
    ]

    search_fields = [
        "title",
        "content"
    ]




class PageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "menu",
        "menu_order",
        "created_at",
        "updated_at",
        "published",
    ]

    list_display_links = [
        "id",
        "title"
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
    



admin.site.register(Page, PageAdmin)
admin.site.register(Article, ArticleAdmin)

# Register your models here.
