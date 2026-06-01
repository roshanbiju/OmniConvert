from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QComboBox,
    QMessageBox
)

from pathlib import Path

from converters.image_converter import ImageConverter


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.current_file = None

        self.setWindowTitle("OmniConvert")
        self.resize(800, 500)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        title = QLabel("OmniConvert")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
        """)

        self.file_label = QLabel(
            "No file selected"
        )

        self.select_button = QPushButton(
            "Select File"
        )

        self.select_button.clicked.connect(
            self.select_file
        )

        self.output_combo = QComboBox()

        self.convert_button = QPushButton(
            "Convert"
        )

        self.convert_button.clicked.connect(
            self.convert_file
        )

        layout.addWidget(title)
        layout.addWidget(self.file_label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.output_combo)
        layout.addWidget(self.convert_button)

        central.setLayout(layout)

    def select_file(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select File"
        )

        if not filename:
            return

        self.current_file = filename

        self.file_label.setText(filename)

        ext = Path(filename).suffix.lower()

        self.output_combo.clear()

        if ext == ".png":
            self.output_combo.addItems(
                ["jpg", "webp"]
            )

        elif ext == ".jpg":
            self.output_combo.addItems(
                ["png", "webp"]
            )

        elif ext == ".webp":
            self.output_combo.addItems(
                ["png", "jpg"]
            )

    def convert_file(self):

        if not self.current_file:
            return

        target = self.output_combo.currentText()

        output = (
            str(
                Path(self.current_file)
                .with_suffix("." + target)
            )
        )

        try:

            ImageConverter.convert(
                self.current_file,
                output
            )

            QMessageBox.information(
                self,
                "Success",
                f"Saved:\n{output}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )