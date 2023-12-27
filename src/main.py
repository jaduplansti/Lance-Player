import flet as ft;

class view():
  def __init__(self, page, controls):
    self.page = page;
    self.views = [];
    self.history = [];
    
    for control in controls:
      control.visible = False;
      self.views.append(control);
      page.add(control);
      
  def change(self, index):
    if index >= len(self.views):
      return;
    if len(self.history) > 0:
      self.history[-1].visible = False;
    if len(self.history) >= 199:
      self.history.clear();
 
    self.views[index].visible = True;
    self.history.append(self.views[index]);

def percent(n, total):
  return (n / 100) * total;
  
def main(page):
  v = view(page, [
    ft.Column(controls = [
      ft.Container(alignment = ft.alignment.center, content = ft.TextField(width = percent(80, page.width), label = "Search", hint_text = "Jojo Music")),
    ]),
    ]);
  v.change(0);
  
  def change_view(e):
    page = e.page;
    index = e.control.selected_index;
    v.change(index);
    page.update();

  page.navigation_bar = ft.NavigationBar(
    destinations = [
      ft.NavigationDestination(icon = ft.icons.FIND_IN_PAGE, label = "Search"),
      ft.NavigationDestination(icon = ft.icons.LIBRARY_MUSIC_OUTLINED, label = "Library"),
    ],
    on_change = change_view,
  );
  page.update();

   
ft.app(target = main, port = 8500, view = ft.AppView.WEB_BROWSER);