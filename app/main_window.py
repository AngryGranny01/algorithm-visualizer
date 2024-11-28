from PySide6.QtWidgets import QMainWindow, QGraphicsScene, QTreeWidgetItem, QPushButton
from PySide6.QtCore import QTimer, Qt
from app.logic.sorting.bubble_sort_stepper import BubbleSortStepper
from app.logic.sorting.quick_sort_stepper import QuickSortStepper
from app.logic.sorting.insertion_sort_stepper import InsertionSortStepper
from app.logic.sorting.selection_sort_stepper import SelectionSortStepper
from app.logic.graph.bfs_stepper import BreadthFirstSearchStepper
from app.logic.graph.dfs_stepper import DepthFirstSearchStepper
from ui.ui_main_window import Ui_MainWindow
from app.visualizers.sorting_visualizer import SortingVisualizer
from app.visualizers.graph_visualizer import GraphVisualizer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize scenes for visualizations
        self.sort_visualizer_scene = QGraphicsScene(self.ui.graphicsView)
        self.graph_visualizer_scene = QGraphicsScene(self.ui.graphicsView)

        # Initialize visualizer logic
        self.sort_visualizer = SortingVisualizer(self.sort_visualizer_scene)
        self.graph_visualizer = GraphVisualizer(self.graph_visualizer_scene)

        # Set the default scene to None
        self.ui.graphicsView.setScene(None)

        self.sort_stepper = None
        self.sort_timer = QTimer(self)
        self.sort_timer.timeout.connect(self.process_next_step)

        self.current_delay = 1500  # Delay in milliseconds between steps
        self.paused = True  # To handle play/pause functionality

        # Define algorithm mapping
        self.algorithms = {
            "Bubble Sort": {
                "stepper": BubbleSortStepper,
                "array": [5, 3, 8, 4, 2],
            },
            "Quick Sort": {
                "stepper": QuickSortStepper,
                "array": [8, 4, 7, 3, 10, 2],
                "partitioning": QuickSortStepper.LOMUTO_PARTITION,
            },
            "Insertion Sort": {
                "stepper": InsertionSortStepper,
                "array": [9, 3, 5, 7, 1],
            },
            "Selection Sort": {
                "stepper": SelectionSortStepper,
                "array": [64, 25, 12, 22, 11],
            },
            "Breadth-First Search": {
                "stepper": BreadthFirstSearchStepper,
                "graph": {
                    0: [1, 2],
                    1: [0, 3, 4],
                    2: [0, 5],
                    3: [1],
                    4: [1, 5],
                    5: [2, 4],
                },
                "start_node": 0,
            },
            "Depth-First Search": {
                "stepper": DepthFirstSearchStepper,
                "graph": {
                    0: [1, 2],
                    1: [3, 4],
                    2: [5],
                    3: [],
                    4: [5],
                    5: [],
                },
                "start_node": 0,
            },
        }

        # Populate tree widget
        self.populate_tree()
        self.ui.treeAlgorithms.itemClicked.connect(self.on_algorithm_selected)

        # Connect button actions
        self.ui.btnStart.clicked.connect(self.start_visualization)
        self.ui.btnStop.clicked.connect(self.stop_visualization)
        self.ui.btnStepForward.clicked.connect(self.step_forward)
        self.ui.btnStepBackward.clicked.connect(self.step_backward)

    def populate_tree(self):
        sorting_category = QTreeWidgetItem(self.ui.treeAlgorithms)
        sorting_category.setText(0, "Sorting")
        for algorithm in ["Bubble Sort", "Quick Sort", "Insertion Sort", "Selection Sort"]:
            QTreeWidgetItem(sorting_category).setText(0, algorithm)

        graph_category = QTreeWidgetItem(self.ui.treeAlgorithms)
        graph_category.setText(0, "Graph Algorithms")
        for algorithm in ["Breadth-First Search", "Depth-First Search"]:
            QTreeWidgetItem(graph_category).setText(0, algorithm)

        self.ui.treeAlgorithms.expandAll()

    def on_algorithm_selected(self, item, column):
        selected_algorithm = item.text(column)
        if selected_algorithm in self.algorithms:
            self.start_algorithm(selected_algorithm)
        else:
            self.ui.textDescription.setPlainText(f"{selected_algorithm} is not implemented yet.")

    def start_algorithm(self, algorithm_name):
        algorithm_config = self.algorithms[algorithm_name]

        if algorithm_name in ["Breadth-First Search", "Depth-First Search"]:
            graph = algorithm_config["graph"]
            start_node = algorithm_config["start_node"]
            self.sort_stepper = algorithm_config["stepper"](graph, start_node)
            self.ui.textDescription.setPlainText(f"Starting {algorithm_name} from node {start_node}")

            # Draw the graph as a tree
            self.graph_visualizer.set_graph(graph, root=start_node)
            self.ui.graphicsView.setScene(self.graph_visualizer_scene)
        else:
            array = algorithm_config["array"]
            self.ui.textDescription.setPlainText(f"Starting {algorithm_name} on array: {array}")

            # Set sorting visualizer scene
            self.sort_visualizer.set_array(array)
            self.ui.graphicsView.setScene(self.sort_visualizer_scene)

            partitioning = algorithm_config.get("partitioning")
            if partitioning:
                self.sort_stepper = algorithm_config["stepper"](array, partitioning)
            else:
                self.sort_stepper = algorithm_config["stepper"](array)

    def start_visualization(self):
        if self.sort_stepper and self.paused:
            self.paused = False
            self.sort_timer.start(self.current_delay)

    def stop_visualization(self):
        if self.sort_stepper and not self.paused:
            self.paused = True
            self.sort_timer.stop()

    def step_forward(self):
        if self.sort_stepper:
            self.process_next_step()

    def step_backward(self):
        if self.sort_stepper and hasattr(self.sort_stepper, "reset"):
            self.sort_stepper.reset()
            self.ui.textDescription.setPlainText("Stepped backward.")

    def process_next_step(self):
        if self.sort_stepper:
            if isinstance(self.sort_stepper, (BreadthFirstSearchStepper, DepthFirstSearchStepper)):
                if not self.sort_stepper.is_complete():
                    # Perform the next step in the traversal
                    step_log = self.sort_stepper.step()
                    self._log_steps(step_log)

                    # Get the last visited node (current node being processed)
                    current_node = self.sort_stepper.visited_order[-1] if self.sort_stepper.visited_order else None
                    if current_node is not None:
                        self.graph_visualizer.highlight_node(current_node, Qt.red)

                    # Highlight previously visited nodes
                    for node in self.sort_stepper.visited_order[:-1]:
                        self.graph_visualizer.highlight_node(node, Qt.green)
                else:
                    # Traversal is complete
                    self.sort_timer.stop()
                    self.ui.textDescription.append(f"Traversal complete! Visited order: {self.sort_stepper.get_visited_order()}")

                    # Highlight the last node in green
                    if self.sort_stepper.visited_order:
                        last_node = self.sort_stepper.visited_order[-1]
                        self.graph_visualizer.highlight_last_node(last_node, Qt.green)
            else:
                if not self.sort_stepper.is_sorted():
                    # Perform the next step in the sorting process
                    step_log, highlights = self.sort_stepper.step()
                    self._log_steps(step_log)

                    # Update sorting visualizer with highlights
                    self.sort_visualizer.update_array(
                        self.sort_stepper.arr,
                        highlights=highlights
                    )
                else:
                    self.sort_timer.stop()
                    self.ui.textDescription.append(f"Sorting complete! Sorted array: {self.sort_stepper.arr}")

    def _log_steps(self, step_log):
        if isinstance(step_log, str):
            self.ui.textDescription.append(step_log)
        elif isinstance(step_log, list):
            for log in step_log:
                self.ui.textDescription.append(log)
