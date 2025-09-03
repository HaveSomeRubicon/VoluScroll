from typing import Callable

from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Listener


class VolumeScroller:
    def __init__(self, paused_callback: Callable[[], bool]) -> None:
        self.paused_callback = paused_callback

        self.middle_mouse_down = False
        self.keyboard_controller = Controller()
        self.listener = Listener(on_scroll=self.on_scroll, on_click=self.on_click)

    def on_scroll(
        self, mouse_x: int, mouse_y: int, direction_x: int, direction_y: int
    ) -> None:
        if not self.middle_mouse_down or self.paused_callback():
            return

        action = Key.media_volume_up if direction_y > 0 else Key.media_volume_down
        self.keyboard_controller.press(action)

    def on_click(
        self, mouse_x: int, mouse_y: int, button: Button, pressed: bool
    ) -> None:
        if button == Button.middle:
            self.middle_mouse_down = pressed

    def start(self) -> None:
        self.listener.start()

    def stop(self) -> None:
        self.listener.stop()
