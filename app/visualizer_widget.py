from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor

class VisualizerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = []

    def set_data(self, data):
        self.data = data
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor("lightblue"))
        for i, value in enumerate(self.data):
            painter.drawRect(i * 40, 100 - value, 30, value)
