import flet as ft;
from flet import TemplateRoute;
from searchview import SearchView;
from playerview import PlayerView;

class View():
  def __init__(self, page, controls):
    self.page = page;
    self.history = [];
    self.controls = [];
    
    for control in controls:
      self.controls.append(control.new());
      
    for control in self.controls:
      control.visible = False;
      self.page.add(control);
  
  def change(self, index):
    if index > len(self.controls):
      return;
    elif len(self.history) > 0:
      self.history[-1].visible = False;
    
    self.controls[index].visible = True;
    self.history.append(self.controls[index]);
    self.page.update();
  
  def get(self, index):
    return self.controls[index];

class Router():
  def __init__(self, page, view):
    self.page = page;
    self.view = view;
    self.info = {};
    self.page.on_route_change = self.change_route;
    self.page.go("/");
    
  def change_route(self, e = None):
    route = e.route;
    match route:
      case "/" | "/player":
        player = self.view.get(0).content.controls;
        if self.exists("current_playing_music"):
          pass;
        else:
          player[0].content.src = "_placeholder/thumbnail.jpg";
          player[3].visible = False;
          self.page.update();

        self.view.change(0);
      
      case "/search":
        self.view.change(1);

    
  def set(self, data):
    self.info.update(data);
  
  def exists(self, key):
    try:
      self.info[key];
      return True;
    except KeyError:
      return False;
      
  def change_destination(self, e):
    index = e.control.selected_index;
    match index:
      case 0:
        self.page.go("/player");
      case 1:
        self.page.go("/search");
      case 2:
        pass;
        
def main(page):
  controls = [PlayerView(page), SearchView(page)];
  view = View(page, controls);
  router = Router(page, view);
  for control in controls:
    control.router = router;
    control.controls = controls;

  page.navigation_bar = ft.NavigationBar(destinations = [
    ft.NavigationDestination(icon = ft.icons.MUSIC_NOTE, label = "Player"),
    ft.NavigationDestination(icon = ft.icons.SEARCH, label = "Search"),
    ft.NavigationDestination(icon = ft.icons.LIBRARY_MUSIC, label = "Library"),
  ],
  on_change = router.change_destination,
  selected_index = None);
  page.update();
  
ft.app(target = main, port = 8500, view = ft.AppView.WEB_BROWSER, assets_dir = "assets");