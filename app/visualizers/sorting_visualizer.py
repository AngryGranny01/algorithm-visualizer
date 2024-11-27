from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem
from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QPen, QColor

class SortingVisualizer:
    def __init__(self, scene):
        self.scene = scene
        self.rects = []  # Store QGraphicsRectItem objects
        self.text_items = []  # Store QGraphicsTextItem for labels
        self.max_value = 1  # Avoid division by zero
        self.scene_width = scene.sceneRect().width()  # Cache the scene width
        self.bar_width = 40
        self.spacing = 5
        self.max_bar_height = 200
        self.y_offset = 250

    def set_array(self, array, bar_color=Qt.gray, label_color=Qt.white, index_color=Qt.lightGray):
        """
        Draw the initial array in the scene.
        """
        self.scene.clear()
        self.rects = []
        self.text_items = []
        self.max_value = max(array) if array else 1

        # Calculate the total width needed and store x_offset for consistent updates
        total_width = len(array) * (self.bar_width + self.spacing) - self.spacing
        self.x_offset = (self.scene_width - total_width) / 2  # Use cached scene width

        # Draw each bar with a label
        for i, value in enumerate(array):
            # Calculate positions and dimensions
            x = self.x_offset + i * (self.bar_width + self.spacing)
            bar_height = (value / self.max_value) * self.max_bar_height  # Scale height
            y = self.y_offset - bar_height

            # Create the bar (rectangle)
            rect = QGraphicsRectItem(QRectF(x, y, self.bar_width, bar_height))
            rect.setBrush(bar_color)
            rect.setPen(QPen(QColor(label_color)))  # Border color
            self.scene.addItem(rect)
            self.rects.append(rect)

            # Create the label (value inside the bar)
            label = QGraphicsTextItem(str(value))
            label.setDefaultTextColor(label_color)
            label.setPos(x + self.bar_width / 4, y + bar_height / 2 - 10)  # Center inside the bar
            self.scene.addItem(label)
            self.text_items.append(label)

            # Add index label above the bar
            index_label = QGraphicsTextItem(str(i))
            index_label.setDefaultTextColor(index_color)
            index_label.setPos(x + self.bar_width / 4, self.y_offset + 10)  # Position above the bar
            self.scene.addItem(index_label)

    def update_array(self, array, highlights=None, bar_color=Qt.gray, compare_color=Qt.red, swap_color=Qt.blue):
        """
        Update the array visualization and highlight specific indices.

        Args:
            array (list): The updated array to visualize.
            highlights (dict): Indices to highlight, e.g., {"compare": [0, 1], "swap": [2, 3]}.
            bar_color (Qt.Color): Default color of the bars.
            compare_color (Qt.Color): Color to use for comparisons.
            swap_color (Qt.Color): Color to use for swaps.
        """
        highlights = highlights or {"compare": [], "swap": []}

        for i, (rect, label) in enumerate(zip(self.rects, self.text_items)):
            # Calculate positions and dimensions
            x = self.x_offset + i * (self.bar_width + self.spacing)
            bar_height = (array[i] / self.max_value) * self.max_bar_height
            y = self.y_offset - bar_height

            # Update the bar's geometry
            rect.setRect(x, y, self.bar_width, bar_height)

            # Highlight the bar based on the action
            if i in highlights.get("compare", []):
                rect.setBrush(compare_color)  # Comparing
            elif i in highlights.get("swap", []):
                rect.setBrush(swap_color)  # Swapping
            else:
                rect.setBrush(bar_color)  # Default color

            # Update the label inside the bar
            label.setPlainText(str(array[i]))
            label.setPos(x + self.bar_width / 4, y + bar_height / 2 - 10)  # Center inside the bar
