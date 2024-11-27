class InsertionSortStepper:
    def __init__(self, arr):
        """
        Initialize the Insertion Sort stepper with the given array.
        """
        self.original_array = arr[:]  # Keep a copy of the original array
        self.arr = arr[:]  # Create a copy to sort
        self.n = len(arr)
        self.i = 1  # Outer loop index starts from 1 (assumes the first element is sorted)
        self.j = 0  # Inner loop index
        self.steps = []  # Log of all operations

    def step(self):
        """
        Perform one step of insertion sort and return the action log and highlights.
        """
        if self.i >= self.n:  # Outer loop complete
            return "Insertion Sort complete!", {"compare": [], "insert": []}

        current = self.arr[self.i]
        self.j = self.i - 1
        highlights = {"compare": [], "insert": []}  # Indices to highlight

        # Shift elements of the sorted part to the right to make space for the current element
        while self.j >= 0 and self.arr[self.j] > current:
            highlights["compare"].append(self.j)  # Highlight comparisons
            self.arr[self.j + 1] = self.arr[self.j]
            self.steps.append(f"Shifted {self.arr[self.j]} to index {self.j + 1}: {self.arr}")
            self.j -= 1

        # Place the current element in its correct position
        self.arr[self.j + 1] = current
        highlights["insert"].append(self.j + 1)  # Highlight the insertion
        self.steps.append(f"Inserted {current} at index {self.j + 1}: {self.arr}")

        # Move to the next element
        self.i += 1

        return self.steps[-1], highlights

    def reset(self):
        """
        Reset the Insertion Sort stepper to its initial state.
        """
        self.arr = self.original_array[:]
        self.i = 1
        self.j = 0
        self.steps = []

    def is_sorted(self):
        """
        Check if the array is fully sorted.
        """
        return self.i >= self.n

    def get_steps(self):
        """
        Get a log of all steps performed so far.
        """
        return self.steps
