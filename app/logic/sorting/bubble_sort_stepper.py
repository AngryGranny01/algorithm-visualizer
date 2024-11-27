class BubbleSortStepper:
    def __init__(self, arr):
        """
        Initialize the Bubble Sort stepper with the given array.
        """
        self.original_array = arr[:]  # Keep a copy of the original array
        self.arr = arr[:]  # Create a working copy for sorting
        self.n = len(arr)
        self.i = 0  # Outer loop index
        self.j = 0  # Inner loop index
        self.steps = []  # Log of all swap operations

    def step(self):
        """
        Perform one step of Bubble Sort and return the step log and highlights.
        """
        if self.i < self.n - 1:  # Outer loop condition
            if self.j < self.n - self.i - 1:  # Inner loop condition
                if self.arr[self.j] > self.arr[self.j + 1]:
                    # Swap elements
                    self.arr[self.j], self.arr[self.j + 1] = self.arr[self.j + 1], self.arr[self.j]
                    swap_info = (self.j, self.j + 1)  # Indices being swapped
                    self.steps.append(swap_info)
                    self.j += 1
                    return f"Swapped index {swap_info[0]} with {swap_info[1]}: {self.arr}", {"compare": [], "swap": swap_info}
                # Just a comparison
                self.j += 1
                return f"Compared index {self.j - 1} with {self.j}: No swap.", {"compare": [self.j - 1, self.j], "swap": []}
            else:
                self.j = 0
                self.i += 1
        return "No swap in this step.", {"compare": [], "swap": []}




    def reset(self):
        """
        Reset the Bubble Sort stepper to its initial state.
        """
        self.arr = self.original_array[:]
        self.i = 0
        self.j = 0
        self.steps = []

    def is_sorted(self):
        """
        Check if the array is fully sorted.
        """
        return self.i >= self.n - 1  # Sorting is complete when outer loop index reaches n-1

    def get_steps(self):
        """
        Get a log of all steps (swaps) performed so far.
        """
        return self.steps
