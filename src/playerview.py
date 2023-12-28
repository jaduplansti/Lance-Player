import flet as ft;
from util import percent;

class PlayerView():
    def __init__(self, page):
        self.page = page;

    def new(self):
        return ft.Container(alignment = ft.alignment.center, content = ft.Column(controls = [
            ft.Container(alignment = ft.alignment.center, content = ft.Image(width = percent(60, self.page.width), height = percent(60, self.page.height))),
            ft.Slider(),
            ft.Row(alignment = ft.MainAxisAlignment.CENTER, spacing = 100, controls = [
                ft.IconButton(icon = ft.icons.SKIP_PREVIOUS),
                ft.IconButton(icon = ft.icons.PLAY_ARROW),
                ft.IconButton(icon = ft.icons.SKIP_NEXT),
            ]),
            ft.Audio(src = None),
        ]));