from typing import Callable

import pystray
from PIL import Image, ImageDraw
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Listener


class VolumeScroller:
    def __init__(self, paused_callback: Callable[[], bool]) -> None:
        self.paused_callback = paused_callback

        self.middle_mouse_down = False
        self.keyboard_controller = Controller()
        self.middle_mouse_down = False
        self.listener = Listener(on_scroll=self.on_scroll, on_click=self.on_click)

    def on_scroll(
        self, mouse_x: int, mouse_y: int, direction_x: int, direction_y: int
    ) -> None:
        if not self.middle_mouse_down or self.paused_callback():
            return
        if direction_y > 0:
            action = Key.media_volume_up
        else:
            action = Key.media_volume_down
        self.keyboard_controller.press(action)

    def on_click(self, mouse_x, mouse_y, button, pressed):
        if not button == Button.middle:
            return
        self.middle_mouse_down = pressed

    def start(self):
        # with self.listener:
        self.listener.start()

    def stop(self):
        self.listener.stop()


class TrayIcon:
    def __init__(self) -> None:
        self.paused = False
        self.icon = pystray.Icon("VoluScroll", self._create_image(), "VoluScroll")
        self.icon.menu = pystray.Menu(
            pystray.MenuItem(
                "Pause", self.toggle_paused, checked=lambda _: self.paused
            ),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Exit", self.stop),
        )

    def _create_image(self) -> Image.Image:
        # simple black square icon
        image = Image.new("RGB", (64, 64), color="black")
        draw = ImageDraw.Draw(image)
        draw.rectangle((16, 16, 48, 48), fill="white")
        return image

    def toggle_paused(self) -> None:
        self.paused = not self.paused

    def start(self) -> None:
        self.icon.run()

    def stop(self) -> None:
        self.icon.stop()


def main() -> None:
    tray_icon = TrayIcon()
    volume_scroller = VolumeScroller(lambda: tray_icon.paused)
    volume_scroller.start()
    tray_icon.start()


if __name__ == "__main__":
    main()
