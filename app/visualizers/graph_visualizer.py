from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsLineItem, QGraphicsTextItem
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPen, QBrush


class GraphVisualizer:
    def __init__(self, scene):
        """
        Initialize the Graph Visualizer.
        :param scene: QGraphicsScene instance to draw the graph.
        """
        self.scene = scene
        self.nodes = {}  # Dictionary to store node positions {node: QPointF}
        self.edges = []  # List of edges [(node1, node2)]
        self.node_items = {}  # Graphics items for nodes {node: QGraphicsEllipseItem}
        self.edge_items = []  # Graphics items for edges [QGraphicsLineItem]
        self.node_radius = 20  # Radius of the node circles
        self.level_spacing = 100  # Vertical spacing between levels
        self.node_spacing = 50  # Horizontal spacing between nodes

    def set_graph(self, graph, root=None):
        """
        Draw the graph as a tree based on the adjacency list.
        :param graph: Dictionary representing the adjacency list of the graph.
        :param root: The root node of the tree (optional). If None, selects the first node as root.
        """
        self.scene.clear()
        self.nodes.clear()
        self.edges.clear()
        self.node_items.clear()
        self.edge_items.clear()

        if root is None:
            root = list(graph.keys())[0]  # Default to the first node if no root is specified

        # Assign positions for nodes in a tree layout
        levels = self._calculate_tree_levels(graph, root)
        self._assign_tree_positions(levels)

        # Draw edges
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                if (neighbor, node) not in self.edges:  # Avoid duplicate edges
                    self.edges.append((node, neighbor))
                    self._draw_edge(node, neighbor)

        # Draw nodes
        for node in graph.keys():
            self._draw_node(node)

    def _calculate_tree_levels(self, graph, root):
        """
        Calculate the levels of the tree for layout purposes.
        :param graph: Dictionary representing the adjacency list.
        :param root: The root node.
        :return: List of levels, where each level contains the nodes at that depth.
        """
        from collections import deque

        levels = []
        visited = set()
        queue = deque([(root, 0)])  # (node, depth)

        while queue:
            node, depth = queue.popleft()
            if node not in visited:
                visited.add(node)
                while len(levels) <= depth:
                    levels.append([])  # Add a new level
                levels[depth].append(node)
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, depth + 1))

        return levels

    def _assign_tree_positions(self, levels):
        """
        Assign positions to nodes based on their levels in the tree.
        :param levels: List of levels, where each level contains the nodes at that depth.
        """
        scene_width = self.scene.sceneRect().width()
        current_y = self.node_radius * 2  # Start just below the top of the scene

        for level in levels:
            level_width = len(level) * (self.node_radius * 2 + self.node_spacing) - self.node_spacing
            start_x = (scene_width - level_width) / 2  # Center the level horizontally
            for i, node in enumerate(level):
                x = start_x + i * (self.node_radius * 2 + self.node_spacing)
                self.nodes[node] = QPointF(x, current_y)
            current_y += self.level_spacing  # Move down for the next level

    def _draw_node(self, node):
        """
        Draw a node on the scene.
        :param node: The node to draw.
        """
        position = self.nodes[node]
        ellipse = QGraphicsEllipseItem(
            position.x() - self.node_radius,
            position.y() - self.node_radius,
            self.node_radius * 2,
            self.node_radius * 2
        )
        ellipse.setBrush(QBrush(Qt.gray))
        ellipse.setPen(QPen(Qt.black))
        self.scene.addItem(ellipse)
        self.node_items[node] = ellipse

        # Add node label
        label = QGraphicsTextItem(str(node))
        label.setDefaultTextColor(Qt.white)
        label.setPos(position.x() - self.node_radius / 2, position.y() - self.node_radius / 2)
        self.scene.addItem(label)

    def _draw_edge(self, node1, node2):
        """
        Draw an edge between two nodes.
        :param node1: Start node.
        :param node2: End node.
        """
        pos1 = self.nodes[node1]
        pos2 = self.nodes[node2]
        line = QGraphicsLineItem(pos1.x(), pos1.y(), pos2.x(), pos2.y())
        line.setPen(QPen(Qt.black, 2))
        self.scene.addItem(line)
        self.edge_items.append(line)

    def highlight_node(self, node, color=Qt.red):
        """
        Highlight a node with a specific color.
        :param node: Node to highlight.
        :param color: QColor to use for highlighting.
        """
        if node in self.node_items:
            self.node_items[node].setBrush(QBrush(color))

    def highlight_last_node(self, node, color=Qt.green):
        """
        Highlight the last node as green after traversal is complete.
        :param node: Node to highlight.
        :param color: QColor to use for highlighting.
        """
        if node in self.node_items:
            self.node_items[node].setBrush(QBrush(color))

    def highlight_edge(self, node1, node2, color=Qt.blue):
        """
        Highlight an edge with a specific color.
        :param node1: Start node of the edge.
        :param node2: End node of the edge.
        :param color: QColor to use for highlighting.
        """
        for edge, (start, end) in zip(self.edge_items, self.edges):
            if (start == node1 and end == node2) or (start == node2 and end == node1):
                edge.setPen(QPen(color, 2))
                break
