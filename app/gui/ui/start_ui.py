from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap, QPainter, QFontMetrics, QColor
from PyQt6.QtCore import Qt

from ...utils import resource_path

# Central widget containing background, label, and button
class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Background image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(resource_path("favicon.png")))
        self.image_label.setScaledContents(True)

        # Version text
        self.version_text_label = QLabel("v0.1.1", self)
        self.version_text_label.setStyleSheet("background-color: transparent; font-weight: bold;")
        self.version_text_label.setFont(QFont("Arial", 16))

        # Start button
        self.start_button = QPushButton("Click Me", self)
        self.start_button.setStyleSheet("background-color: transparent;")

    # Resize event to reposition widgets
    def resizeEvent(self, a0=None):
        size = self.size()

        # Center background image
        img_width, img_height = 600, 600
        self.image_label.resize(img_width, img_height)
        self.image_label.move(
            (size.width() - img_width) // 2,
            (size.height() - img_height) // 2
        )

        # Center rotated label
        self.version_text_label.move(
            int((size.width() - self.version_text_label.width()) / 2),
            int((size.height() - self.version_text_label.height()) / 2 + self.image_label.height() / 8)
        )

        # Center button below label
        btn_width, btn_height = 200, 50
        self.start_button.setGeometry(
            (size.width() - btn_width) // 2,
            (size.height() // 2) + 120,
            btn_width,
            btn_height
        )

        super().resizeEvent(a0)

# Start screen UI wrapper
class StartScreenUI:
    def setup_ui(self, window):
        self.central_widget = CentralWidget()
        window.setCentralWidget(self.central_widget)