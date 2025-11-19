import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtGui import QIcon, QPixmap

from .gui.ui.start_ui import StartScreenUI
from .gui.controllers.start_controller import StartScreenController
from .utils import windows_config, resource_path, ScreenManager


def start_gui():
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("ANorm")
    window.setStyleSheet("background-color: white;")

    # Create the stacked widget FIRST
    stacked = QStackedWidget()
    window.setCentralWidget(stacked)

    # Set up the ScreenManager
    manager = ScreenManager(stacked)

    screens = [
        ("start", StartScreenUI, StartScreenController),
    ]

    for name, UIClass, ControllerClass in screens:
        ui = UIClass()
        ui.setup_ui()
        controller = ControllerClass(ui, manager)
        manager.add_screen(name, ui.central_widget, controller)
    
    manager.show("start")
    window.showMaximized()

    if sys.platform == "win32":
        windows_config(window)
    elif sys.platform == "darwin":
        app.setWindowIcon(QIcon(QPixmap(resource_path("favicon.icns"))))
    else:
        app.setWindowIcon(QIcon(QPixmap(resource_path("favicon.png"))))

    sys.exit(app.exec())