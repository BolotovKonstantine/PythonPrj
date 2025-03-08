import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QLinearGradient, QBrush, QColor, QFont
from PyQt5.QtCore import Qt, QRect


class FancyHelloWorld(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World Window")
        self.resize(400, 300)

        # Central widget to hold our layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Hello World label
        self.title_label = QLabel("Hello, World!", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))

        # Copyright label
        self.copyright_label = QLabel("© Konstantin Bolotov", self)
        copyright_font = QFont("Arial", 10)
        copyright_font.setItalic(True)

        # Align text in the center horizontally but keep it near bottom with layout
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setFont(copyright_font)

        # Add widgets to the layout
        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(copyright_label)

    def paintEvent(self, event):
        """Override paintEvent to draw a gradient background."""
        painter = QPainter(self)
        rect = self.rect()

        # Create linear gradient
        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        gradient.setColorAt(0, QColor(100, 140, 230))
        gradient.setColorAt(1, QColor(60, 100, 200))

        painter.fillRect(rect, QBrush(gradient))


def main():
    app = QApplication(sys.argv)
    window = FancyHelloWorld()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()