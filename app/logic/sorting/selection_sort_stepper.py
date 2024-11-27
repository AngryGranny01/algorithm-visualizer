class SelectionSortStepper:
    def __init__(self, arr):
        """
        Initialize the Selection Sort stepper with the given array.
        """
        self.original_array = arr[:]  # Keep a copy of the original array
        self.arr = arr[:]  # Create a working copy for sorting
        self.n = len(arr)
        self.i = 0  # Outer loop index
        self.smallest_index = 0  # Index of the smallest element in the current iteration
        self.steps = []  # Log of all operations

    def step(self):
        """
        Perform one step of selection sort and return the step log and highlighted indices.
        """
        if self.i >= self.n - 1:  # If the outer loop is complete, the array is sorted
            return "Selection Sort complete!", {"compare": [], "swap": []}

        step_logs = []  # Collect logs for this step
        highlights = {"compare": [], "swap": []}  # Highlight indices for visualization

        # Find the smallest element in the unsorted portion of the array
        self.smallest_index = self.i
        for j in range(self.i + 1, self.n):
            highlights["compare"].append(j)  # Highlight the current comparison
            if self.arr[j] < self.arr[self.smallest_index]:
                self.smallest_index = j

        step_logs.append(f"Found smallest number {self.arr[self.smallest_index]} at index {self.smallest_index}.")

        # Swap the smallest element with the first unsorted element if needed
        if self.smallest_index != self.i:
            self.arr[self.i], self.arr[self.smallest_index] = self.arr[self.smallest_index], self.arr[self.i]
            highlights["swap"] = [self.i, self.smallest_index]
            step_logs.append(f"Swapped index {self.i} with {self.smallest_index}: {self.arr}")
        else:
            step_logs.append(f"No swap needed for index {self.i}: {self.arr}")

        # Move to the next position in the array
        self.i += 1

        # Return logs and highlights for visualization
        return step_logs, highlights

    def reset(self):
        """
        Reset the Selection Sort stepper to its initial state.
        """
        self.arr = self.original_array[:]
        self.i = 0
        self.smallest_index = 0
        self.steps = []

    def is_sorted(self):
        """
        Check if the array is fully sorted.
        """
        return self.i >= self.n - 1

    def get_steps(self):
        """
        Get a log of all steps performed so far.
        """
        return self.steps
