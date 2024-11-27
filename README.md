# Algorithm Visualizer

A Python-based algorithm visualizer built with **PySide6**, offering a graphical representation of sorting and graph traversal algorithms. This interactive tool is designed for learning and teaching algorithm concepts in an engaging and intuitive way.

---

## Features

### Sorting Algorithms

- **Bubble Sort**: Visualize how elements are swapped iteratively until the array is sorted.
- **Quick Sort**: Observe the divide-and-conquer approach with various partitioning schemes.
- **Insertion Sort**: Step through the insertion of elements into a sorted portion.
- **Selection Sort**: Follow the process of selecting and swapping the smallest elements.

### Graph Algorithms

- **Breadth-First Search (BFS)**: Explore nodes level by level in a graph.
- **Depth-First Search (DFS)**: Traverse through graph paths deeply before backtracking.

### General Features

- Dynamic visualization of algorithm steps.
- Highlights key operations like comparisons, swaps, and visited nodes.
- Customizable input for arrays (sorting) and graphs (traversal).

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- **PySide6**: A Python binding for the Qt toolkit.

### Steps to Install and Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AngryGranny01/algorithm-visualizer.git
   cd algorithm-visualizer
   ```

2. **Set Up a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate    # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python main.py
   ```

---

## Usage

1. Launch the application.
2. Select an algorithm from the left-hand menu:
   - **Sorting Algorithms**: Visualize step-by-step sorting of an array.
   - **Graph Algorithms**: Observe graph traversal processes.
3. Customize inputs for arrays or graphs to explore different cases.
4. Watch the visualization and logs update dynamically for each algorithm step.

---

## Project Structure

```plaintext
algorithm-visualizer/
│
├── app/
│   ├── logic/                # Algorithm implementations (sorting and graph traversal)
│   ├── visualizers/          # Visualization logic for rendering algorithms
│   ├── main_window.py        # Core application logic
│
├── ui/
│   ├── ui_main_window.py     # Generated UI file (from .ui file)
│   ├── main_window.ui        # Original Qt Designer file
│
├── resources.qrc             # Resource file for assets
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation
├── LICENSE                   # License file (if applicable)
└── main.py                   # Entry point of the application
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
