import pystray
from PIL import Image, ImageDraw


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
