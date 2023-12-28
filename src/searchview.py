import flet as ft;
from music import Music;
from util import percent;

class SearchView():
  def __init__(self, page):
    self.page = page;
    self.router = None;
    self.controls = None;
    self.suggestions = ft.Ref[ft.Column]();
    self.suggestcontainer = ft.Ref[ft.Container]();
    
  def new(self): # fix this
    return ft.Container(width = percent(100, self.page.width), height = percent(100, self.page.height), content = ft.Column(controls = [
      ft.Container(alignment = ft.alignment.center, content = ft.TextField(width = percent(80, self.page.width), label = "Search", hint_text = "Jojo Music", on_change = self.suggest)),
      ft.Container(ref = self.suggestcontainer, content = ft.Column(ref = self.suggestions, width = percent(100, self.page.width), height = percent(50, self.page.height), scroll = ft.ScrollMode.ALWAYS)),
    ]));

  def redirect_player(self, e):
    self.controls

  def suggest(self, e):
    text = e.control.value;
    self.suggestions.current.controls.clear();
    if len(text) > 0:
      for music in Music().search(text):
        self.suggestions.current.controls.append(ft.Text(music["title"]));
      self.suggestcontainer.current.visible = True;
    else:
      self.suggestcontainer.current.visible = False;
    
    self.page.update();