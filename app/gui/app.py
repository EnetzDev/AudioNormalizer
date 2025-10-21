import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

from .ui.start_screen_ui import StartScreenUI
from .controllers.start_screen_controller import StartScreenController
from app.core.utils import resource_path

def start_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Audio Normalizer")
    window.setWindowIcon(QIcon(resource_path("logo.png")))

    # Set up the UI
    ui = StartScreenUI()
    ui.setup_ui(window)

    # Connect UI with logic
    controller = StartScreenController(ui)

    # Maximize
    window.showMaximized()

    # Show window and start the event loop
    window.show()
    sys.exit(app.exec())