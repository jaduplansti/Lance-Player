import flet as ft;
from music import Music;

class SearchView(ft.UserControl):
    def build(self):
        return ft.Column(controls = [
            ft.TextField(label = "Search", hint_text = "Jotaro Theme")
        ]);