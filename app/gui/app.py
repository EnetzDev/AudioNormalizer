import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap

from .ui.start_screen_ui import StartScreenUI
from .controllers.start_screen_controller import StartScreenController
from .utils import windows_config


def start_gui():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("ANorm")

    # Set up the UI
    ui = StartScreenUI()
    ui.setup_ui(window)

    # Connect UI with logic
    controller = StartScreenController(ui)

    # Show window
    window.show()
    window.showMaximized()

    if sys.platform == "win32":
        windows_config(window)
    elif sys.platform == "darwin":
        app.setWindowIcon(QIcon(QPixmap(resource_path("icon.icns"))))
    else:
        app.setWindowIcon(QIcon(QPixmap(resource_path("icon.png"))))

    sys.exit(app.exec())