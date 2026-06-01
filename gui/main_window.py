from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OmniConvert")
        self.resize(900, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        title = QLabel("OmniConvert")
        title.setStyleSheet(
            "font-size: 24px;"
            "font-weight: bold;"
        )

        layout.addWidget(title)

        central_widget.setLayout(layout)