import flet as ft;
from music import Music;
from util import percent;

class SearchView():
  def __init__(self, page):
    self.page = page;
    self.router = None;
    self.suggestions = ft.Ref[ft.Column]();
    
  def new(self):
    return ft.Container(alignment = ft.alignment.center, content = ft.Column(ref = self.suggestions, controls = [
      ft.TextField(width = percent(80, self.page.width), label = "Search", hint_text = "Jojo Music", on_change = self.suggest),
    ]));
    
  def suggest(self, e):
    text = e.control.value;
    if len(text) > 0:
      for music in Music().search(text):
        pass;