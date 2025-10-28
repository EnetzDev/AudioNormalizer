import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap

from .gui.ui.start_ui import StartScreenUI
from .gui.controllers.start_controller import StartScreenController
from .utils import windows_config, resource_path


def start_gui():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("ANorm")
    window.setStyleSheet("background-color: white;")

    window.show()
    window.showMaximized()

    if sys.platform == "win32":
        windows_config(window)
    elif sys.platform == "darwin":
        app.setWindowIcon(QIcon(QPixmap(resource_path("favicon.icns"))))
    else:
        app.setWindowIcon(QIcon(QPixmap(resource_path("favicon.png"))))

    # Set up the UI
    ui = StartScreenUI()
    ui.setup_ui(window)

    # Connect UI with logic
    controller = StartScreenController(ui)

    sys.exit(app.exec())