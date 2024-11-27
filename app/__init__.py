# app/__init__.py
# This file marks the directory as a package

__version__ = "1.0.0"

from .main_window import MainWindow
from .logic.sorting.bubble_sort_stepper import BubbleSortStepper
from .visualizer_widget import VisualizerWidget