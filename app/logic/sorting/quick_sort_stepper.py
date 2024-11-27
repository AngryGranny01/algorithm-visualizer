class QuickSortStepper:
    NAIVE_PARTITION = "NAIVE"
    LOMUTO_PARTITION = "LOMUTO"
    HOARES_PARTITION = "HOARES"

    def __init__(self, arr, partitioning_method=NAIVE_PARTITION):
        """
        Initialize the QuickSort stepper with the given array.
        """
        self.original_array = arr[:]  # Keep a copy of the original array
        self.arr = arr[:]  # Operate on a copy
        self.partitioning_method = partitioning_method  # Chosen partitioning strategy
        self.steps = []  # Log of all steps
        self.stack = [(0, len(arr) - 1)]  # Simulate the recursive stack for QuickSort

    def partition(self, low, high):
        """
        Partition the array based on the selected partitioning method.
        """
        if self.partitioning_method == QuickSortStepper.NAIVE_PARTITION:
            return self.naive_partition(low, high)
        elif self.partitioning_method == QuickSortStepper.LOMUTO_PARTITION:
            return self.lomuto_partition(low, high)
        elif self.partitioning_method == QuickSortStepper.HOARES_PARTITION:
            return self.hoare_partition(low, high)
        else:
            raise ValueError(f"Invalid partitioning method: {self.partitioning_method}")

    def naive_partition(self, low, high):
        """
        Naive partition: Create two temporary arrays to sort elements around the pivot.
        """
        pivot = self.arr[high]
        smaller = [x for x in self.arr[low:high] if x <= pivot]
        greater = [x for x in self.arr[low:high] if x > pivot]
        self.arr[low : high + 1] = smaller + [pivot] + greater
        self.steps.append(f"Naively partitioned with pivot {pivot}: {self.arr}")
        return low + len(smaller), {"pivot": [high], "compare": [], "swap": []}

    def lomuto_partition(self, low, high):
        """
        Lomuto partition: Use the last element as the pivot.
        """
        pivot = self.arr[high]
        i = low - 1  # Pointer for the smaller element
        highlights = {"pivot": [high], "compare": [], "swap": []}
        for j in range(low, high):
            highlights["compare"].append(j)
            if self.arr[j] <= pivot:
                i += 1
                # Swap elements
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                highlights["swap"] = [i, j]
                self.steps.append(f"Swapped {self.arr[i]} with {self.arr[j]}: {self.arr}")
        # Place the pivot element in the correct position
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        highlights["swap"] = [i + 1, high]
        self.steps.append(f"Moved pivot {pivot} to index {i + 1}: {self.arr}")
        return i + 1, highlights

    def hoare_partition(self, low, high):
        """
        Hoare partition: Use a two-pointer approach.
        """
        pivot = self.arr[low]
        i = low - 1
        j = high + 1
        highlights = {"pivot": [low], "compare": [], "swap": []}

        while True:
            # Move i to the right
            while True:
                i += 1
                highlights["compare"].append(i)
                if self.arr[i] >= pivot:
                    break

            # Move j to the left
            while True:
                j -= 1
                highlights["compare"].append(j)
                if self.arr[j] <= pivot:
                    break

            # If pointers cross, return partition index
            if i >= j:
                self.steps.append(f"Partitioned around pivot {pivot}: {self.arr}")
                return j, highlights

            # Swap elements
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            highlights["swap"] = [i, j]
            self.steps.append(f"Swapped {self.arr[i]} with {self.arr[j]}: {self.arr}")

    def step(self):
        """
        Perform one step of QuickSort and return the step log and highlights.
        """
        if not self.stack:
            return "QuickSort complete!", {"pivot": [], "compare": [], "swap": []}

        # Simulate recursive QuickSort using a stack
        low, high = self.stack.pop()
        if low < high:
            pivot_index, highlights = self.partition(low, high)

            # Push subproblems onto the stack for further processing
            if pivot_index - 1 > low:
                self.stack.append((low, pivot_index - 1))
            if pivot_index + 1 < high:
                self.stack.append((pivot_index + 1, high))

            return self.steps[-1], highlights
        return "No operation performed.", {"pivot": [], "compare": [], "swap": []}

    def is_sorted(self):
        """
        Check if the sorting is complete.
        """
        return not self.stack

    def reset(self):
        """
        Reset the sorter to the initial state.
        """
        self.arr = self.original_array[:]
        self.steps = []
        self.stack = [(0, len(self.arr) - 1)]

    def get_steps(self):
        """
        Get a log of all steps performed so far.
        """
        return self.steps
