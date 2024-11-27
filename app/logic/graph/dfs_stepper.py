class DepthFirstSearchStepper:
    def __init__(self, graph, start_node):
        """
        Initialize the DFS stepper.
        :param graph: Dictionary representing the adjacency list of the graph.
        :param start_node: The starting node for DFS.
        """
        self.graph = graph
        self.start_node = start_node
        self.stack = [start_node]  # DFS stack
        self.visited = set()  # Set to track visited nodes
        self.visited_order = []  # Order of visited nodes
        self.steps = []  # Log of all steps

    def step(self):
        """
        Perform one step of DFS and return the log of the step.
        """
        self.steps = []
        if not self.stack:
            return "DFS complete!"  # If the stack is empty, DFS is complete.

        current_node = self.stack.pop()

        if current_node not in self.visited:
            # Log visiting the node
            self.visited.add(current_node)
            self.visited_order.append(current_node)
            self.steps.append(f"Visited node {current_node}")

            # Add unvisited neighbors to the stack (in reverse order for correct DFS order)
            for neighbor in reversed(self.graph.get(current_node, [])):
                if neighbor not in self.visited:
                    self.stack.append(neighbor)
                    self.steps.append(f"Queued neighbor {neighbor} from node {current_node}")
        return self.steps

    def is_complete(self):
        """
        Check if DFS is complete (stack is empty).
        """
        return not self.stack

    def reset(self):
        """
        Reset the DFS stepper to its initial state.
        """
        self.stack = [self.start_node]
        self.visited = set()
        self.visited_order = []
        self.steps = []

    def get_visited_order(self):
        """
        Get the order in which nodes were visited.
        """
        return self.visited_order
