import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from .ui.start_screen_ui import StartScreenUI
from .controllers.start_screen_controller import StartScreenController

def start_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()

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