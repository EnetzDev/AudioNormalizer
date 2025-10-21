from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout

class StartScreenUI:
    def setup_ui(self, window):

        # Central widget
        central_widget = QWidget()
        window.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Button
        self.start_button = QPushButton("Click Me")
        layout.addWidget(self.start_button)