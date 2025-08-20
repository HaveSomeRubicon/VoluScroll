from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Listener


class VolumeScroller:
    def __init__(self) -> None:
        self.keyboard_controller = Controller()
        self.middle_mouse_down = False
        self.listener = Listener(on_scroll=self.on_scroll, on_click=self.on_click)

    def on_scroll(self, mouse_x, mouse_y, direction_x, direction_y):
        if not self.middle_mouse_down:
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


if __name__ == "__main__":
    volume_scroller = VolumeScroller()
    volume_scroller.start()
