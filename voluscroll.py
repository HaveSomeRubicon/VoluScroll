from pynput.mouse import Listener
from pynput.keyboard import Key, Controller


keyboard_controller = Controller()
middle_mouse_down = False

def on_scroll(mouse_x, mouse_y, direction_x, direction_y):
    print(f"MOUSE X: {mouse_x}, MOUSE Y: {mouse_y}, Direction X: {direction_x}, Direction Y: {direction_y}")
    if middle_mouse_down == True:
        if direction_y > 0:
            action = Key.media_volume_up
        elif direction_y < 0:
            action = Key.media_volume_down
        keyboard_controller.press(action)


def on_click(mouse_x, mouse_y, button, pressed):
    print(f"MOUSE X: {mouse_x}, MOUSE Y: {mouse_y}, Button: {button}, Pressed: {pressed}")
    global middle_mouse_down
    middle_mouse_down = pressed

listener = Listener(on_scroll=on_scroll, on_click=on_click)

with listener:
    listener.join()