from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem
from PySide6.QtCore import Qt, QPointF

class GraphVisualizer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.node_items = {}  # Maps node IDs to graphical items
        self.edge_items = []  # List of edge graphical items

        self.node_radius = 20  # Radius of each node
        self.spacing = 100  # Spacing between nodes (used for layout)

    def set_graph(self, graph):
        """
        Set the graph to visualize and draw the initial state.
        Graph should be in adjacency list format:
        {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 5],
            ...
        }
        """
        self.scene.clear()
        self.node_items = {}
        self.edge_items = []

        # Create a circular layout for simplicity
        num_nodes = len(graph)
        center = QPointF(self.width() / 2, self.height() / 2)
        angle_step = 360 / max(1, num_nodes)  # Avoid division by zero

        positions = {}

        # Draw nodes
        for i, node in enumerate(graph.keys()):
            angle = angle_step * i
            x = center.x() + self.spacing * (num_nodes ** 0.5) * Qt.sin(Qt.radians(angle))
            y = center.y() - self.spacing * (num_nodes ** 0.5) * Qt.cos(Qt.radians(angle))
            position = QPointF(x, y)

            # Draw node circle
            ellipse = QGraphicsEllipseItem(-self.node_radius, -self.node_radius, self.node_radius * 2, self.node_radius * 2)
            ellipse.setBrush(Qt.blue)
            ellipse.setPen(Qt.black)
            ellipse.setPos(position)
            self.scene.addItem(ellipse)

            # Draw node label
            text = QGraphicsTextItem(str(node))
            text.setDefaultTextColor(Qt.white)
            text.setPos(position.x() - self.node_radius / 2, position.y() - self.node_radius / 2)
            self.scene.addItem(text)

            self.node_items[node] = (ellipse, text)
            positions[node] = position

        # Draw edges
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                if (node, neighbor) not in self.edge_items and (neighbor, node) not in self.edge_items:
                    line = QGraphicsLineItem(
                        positions[node].x(), positions[node].y(),
                        positions[neighbor].x(), positions[neighbor].y()
                    )
                    line.setPen(Qt.black)
                    self.scene.addItem(line)
                    self.edge_items.append((node, neighbor, line))

        self.setSceneRect(self.scene.itemsBoundingRect())

    def highlight_node(self, node, color=Qt.red):
        """
        Highlight a specific node with the given color.
        """
        if node in self.node_items:
            ellipse, _ = self.node_items[node]
            ellipse.setBrush(color)

    def highlight_edge(self, node1, node2, color=Qt.red):
        """
        Highlight a specific edge between two nodes with the given color.
        """
        for edge in self.edge_items:
            if (edge[0] == node1 and edge[1] == node2) or (edge[0] == node2 and edge[1] == node1):
                line = edge[2]
                line.setPen(color)
                break

    def clear_highlights(self):
        """
        Reset all highlights to the default colors.
        """
        for node, (ellipse, _) in self.node_items.items():
            ellipse.setBrush(Qt.blue)

        for edge in self.edge_items:
            line = edge[2]
            line.setPen(Qt.black)
