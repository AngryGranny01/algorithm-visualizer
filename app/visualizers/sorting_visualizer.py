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
        self.box_width = 50
        self.box_height = 40
        self.spacing = 5
        self.y_offset = 100  # Vertical position for the row of boxes

    def set_array(self, array, box_color=Qt.lightGray, label_color=Qt.black):
        """
        Draw the initial array in the scene.
        """
        self.scene.clear()
        self.rects = []
        self.text_items = []
        self.max_value = max(array) if array else 1

        # Calculate the total width needed and store x_offset for consistent updates
        total_width = len(array) * (self.box_width + self.spacing) - self.spacing
        self.x_offset = (self.scene_width - total_width) / 2  # Use cached scene width

        # Draw each box with a label
        for i, value in enumerate(array):
            # Calculate positions and dimensions
            x = self.x_offset + i * (self.box_width + self.spacing)

            # Create the box (rectangle)
            rect = QGraphicsRectItem(QRectF(x, self.y_offset, self.box_width, self.box_height))
            rect.setBrush(QColor(box_color))
            rect.setPen(QPen(Qt.black))  # Border color
            self.scene.addItem(rect)
            self.rects.append(rect)

            # Create the label (value inside the box)
            label = QGraphicsTextItem(str(value))
            label.setDefaultTextColor(QColor(label_color))
            label.setPos(x + self.box_width / 4, self.y_offset + self.box_height / 4)  # Center inside the box
            self.scene.addItem(label)
            self.text_items.append(label)

    def update_array(self, array, highlights=None, box_color=Qt.lightGray, compare_color=Qt.red, swap_color=Qt.blue):
        """
        Update the array visualization and highlight specific indices.

        Args:
            array (list): The updated array to visualize.
            highlights (dict): Indices to highlight, e.g., {"compare": [0, 1], "swap": [2, 3]}.
            box_color (Qt.Color): Default color of the boxes.
            compare_color (Qt.Color): Color to use for comparisons.
            swap_color (Qt.Color): Color to use for swaps.
        """
        highlights = highlights or {"compare": [], "swap": []}

        for i, (rect, label) in enumerate(zip(self.rects, self.text_items)):
            # Calculate positions
            x = self.x_offset + i * (self.box_width + self.spacing)

            # Update the box's geometry (optional, if array size changes dynamically)
            rect.setRect(x, self.y_offset, self.box_width, self.box_height)

            # Highlight the box based on the action
            if i in highlights.get("compare", []):
                rect.setBrush(QColor(compare_color))  # Comparing
            elif i in highlights.get("swap", []):
                rect.setBrush(QColor(swap_color))  # Swapping
            else:
                rect.setBrush(QColor(box_color))  # Default color

            # Update the label inside the box
            label.setPlainText(str(array[i]))
            label.setPos(x + self.box_width / 4, self.y_offset + self.box_height / 4)  # Center inside the box
