from sevo_pages.models import Menu, Page


class PageChecker():
    def __init__(self, path, page):
        self.path = path
        self.page = page

    def is_active_page(self):
        return self.page.get_absolute_url() == self.path



def menus_context(request):
    menus = Menu.objects.all()
    menu_main = menus.get(name="Main")
    menu_meta = menus.get(name="Meta")

    homepage = Page.get_home_page()


    return {
        "menus": menus,
        "menu_main": menu_main,
        "menu_meta": menu_meta, 
        "homepage": homepage
    }
    