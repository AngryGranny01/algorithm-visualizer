from collections import deque

class BreadthFirstSearchStepper:
    def __init__(self, graph, start_node):
        """
        Initialize the BFS stepper.
        :param graph: Dictionary representing the adjacency list of the graph.
        :param start_node: The starting node for BFS.
        """
        self.graph = graph
        self.start_node = start_node
        self.queue = deque([start_node])  # BFS queue
        self.visited = set()  # Set to track visited nodes
        self.visited_order = []  # Order of visited nodes
        self.steps = []  # Log of all steps

    def step(self):
        """
        Perform one step of BFS and return the log of the step.
        """
        self.steps = []
        
        if not self.queue:
            return "BFS complete!"  # If the queue is empty, BFS is complete.

        current_node = self.queue.popleft()

        if current_node not in self.visited:
            # Log visiting the node
            self.visited.add(current_node)
            self.visited_order.append(current_node)
            self.steps.append(f"Visited node {current_node}")

            # Add unvisited neighbors to the queue
            for neighbor in self.graph.get(current_node, []):
                if neighbor not in self.visited and neighbor not in self.queue:
                    self.queue.append(neighbor)
                    self.steps.append(f"Queued neighbor {neighbor} from node {current_node}")

        return self.steps

    def is_complete(self):
        """
        Check if BFS is complete (queue is empty).
        """
        return not self.queue

    def reset(self):
        """
        Reset the BFS stepper to its initial state.
        """
        self.queue = deque([self.start_node])
        self.visited = set()
        self.visited_order = []
        self.steps = []

    def get_visited_order(self):
        """
        Get the order in which nodes were visited.
        """
        return self.visited_order
