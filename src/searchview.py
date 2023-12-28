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
    
  def new(self):
    return ft.Container(ref = self.suggestcontainer, alignment = ft.alignment.center, content = ft.Column(ref = self.suggestions, controls = [
      ft.TextField(width = percent(80, self.page.width), label = "Search", hint_text = "Jojo Music", on_change = self.suggest),
    ]));

  def redirect_player(self, e):
    self.controls

  def suggest(self, e):
    text = e.control.value;
    if len(text) > 0:
      for music in Music().search(text):
        pass;