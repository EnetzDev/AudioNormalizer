class StartScreenController:
    def __init__(self, ui, manager):
        self.ui = ui
        self.manager = manager
        self.ui.central_widget.analyze_button.clicked.connect(self.on_start_clicked)
        self.ui.central_widget.normalize_button.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        print("Start button clicked!")