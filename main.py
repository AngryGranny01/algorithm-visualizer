import sys
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow  # Import your MainWindow class

def main():
    # Create the application instance
    app = QApplication(sys.argv)
    
    # Create the main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
