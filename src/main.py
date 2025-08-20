from .tray_icon import TrayIcon
from .volume_scroller import VolumeScroller


def main() -> None:
    tray_icon = TrayIcon()
    volume_scroller = VolumeScroller(lambda: tray_icon.paused)
    volume_scroller.start()
    tray_icon.start()


if __name__ == "__main__":
    main()
