class StartScreenController:
    def __init__(self, ui):
        self.ui = ui
        self.ui.start_button.clicked.connect(self.on_start_clicked)

    def on_start_clicked(self):
        print("Start button clicked!")