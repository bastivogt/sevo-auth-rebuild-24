from . import settings

from .models import Menu, Page



def menus_context(request):
    menus = Menu.objects.all()
    menu_main = menus.get(name=settings.SEVO_PAGES_MENU_MAIN)
    menu_meta = menus.get(name=settings.SEVO_PAGES_MENU_META)

    homepage = Page.get_home_page()


    return {
        "menus": menus,
        "menu_main": menu_main,
        "menu_meta": menu_meta, 
        "homepage": homepage
    }
    