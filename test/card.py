import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPainter, QColor, QLinearGradient
from PyQt5.QtCore import Qt

class CardButton(QWidget):
    def __init__(self, title, instance_count, parent=None):
        super().__init__(parent)

        self.title = title
        self.instance_count = instance_count

        # Create labels
        self.titleLabel = QLabel(title, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.instanceLabel = QLabel(str(instance_count), alignment=Qt.AlignBottom | Qt.AlignLeft)

        # Set font sizes
        self.titleLabel.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.instanceLabel.setStyleSheet("font-size: 12px;")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.instanceLabel)
        self.setLayout(layout)

    def paintEvent(self, event):
        # Custom paint event to draw gradient background
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(230, 230, 230))
        gradient.setColorAt(1, QColor(200, 200, 200))
        painter.setBrush(gradient)
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        # Override mouse press event to capture click
        print("Hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create instances of CardButton
    card1 = CardButton("Card 1", 10)
    card2 = CardButton("Card 2", 20)

    # Set up main window
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(card1)
    layout.addWidget(card2)
    window.setLayout(layout)

    window.setGeometry(100, 100, 400, 300)
    window.show()

    sys.exit(app.exec_())
