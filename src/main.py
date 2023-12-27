import flet as ft;
from searchview import SearchView;

def main(page):
    def change_view(e):
        page = e.page;
        index = e.control.selected_index;
        match index:
            case 0:
                page.views.append(ft.View(controls = [SearchView()]));
        
        page.update();

    page.add(ft.NavigationBar(
        destinations = [
            ft.NavigationDestination(icon = ft.icons.FIND_IN_PAGE, label = "Search"),
            ft.NavigationDestination(icon = ft.icons.LIBRARY_MUSIC_OUTLINED, label = "Library"),
        ],
        on_change = change_view,
    ));

   
ft.app(target = main, port = 8500, view = ft.AppView.WEB_BROWSER);