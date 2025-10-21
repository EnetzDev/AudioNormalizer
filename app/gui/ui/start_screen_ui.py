from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont

from app.core.utils import get_version

class StartScreenUI:
    def setup_ui(self, window):

        # Central widget
        central_widget = QWidget()
        window.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Version Label
        version_text_font = QFont()
        version_text_font.setPointSize(48)

        self.version_text_label = QLabel("v" + get_version())
        self.version_text_label.setFont(version_text_font)

        layout.addWidget(self.version_text_label)

        # Button
        self.start_button = QPushButton("Click Me")
        layout.addWidget(self.start_button)