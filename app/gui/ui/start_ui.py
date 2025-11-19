from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap

from ...utils import resource_path  # keep your resource loader

# Central widget containing background, label, and buttons
class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Background image
        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(resource_path("favicon.png")))
        self.image_label.setScaledContents(True)

        # Version text
        self.version_text_label = QLabel("v0.1.5", self)
        self.version_text_label.setStyleSheet(
            "background-color: transparent; font-weight: bold;"
        )
        self.version_text_label.setFont(QFont("Arial", 16))

        # Buttons
        self.analyze_button = QPushButton("Analyze Audio", self)
        self.analyze_button.setStyleSheet("background-color: transparent;")

        self.normalize_button = QPushButton("Normalize Audio", self)
        self.normalize_button.setStyleSheet("background-color: transparent;")

    def resizeEvent(self, a0):
        size = self.size()

        # Center background image
        img_width, img_height = 600, 600
        self.image_label.resize(img_width, img_height)
        self.image_label.move(
            (size.width() - img_width) // 2,
            (size.height() - img_height) // 2,
        )

        # Center version label slightly above middle
        self.version_text_label.adjustSize()
        self.version_text_label.move(
            (size.width() - self.version_text_label.width()) // 2,
            (size.height() - self.version_text_label.height()) // 2
            + self.image_label.height() // 8,
        )

        # Buttons below label
        btn_width, btn_height = 200, 50
        self.analyze_button.setGeometry(
            (size.width() - btn_width) // 2 - 100,
            (size.height() // 2) + 120,
            btn_width,
            btn_height,
        )
        self.normalize_button.setGeometry(
            (size.width() - btn_width) // 2 + 100,
            (size.height() // 2) + 120,
            btn_width,
            btn_height,
        )

        super().resizeEvent(a0)


# UI wrapper for StartScreen
class StartScreenUI:
    def setup_ui(self):
        self.central_widget = CentralWidget()