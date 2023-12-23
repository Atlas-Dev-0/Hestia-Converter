import sys
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from python_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip


class hestiaMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.import_button.clicked.connect(self.browse_file)
        self.save_button.clicked.connect(self.saveTo_file)
        self.convert_button.clicked.connect(self.saveTo_file)

    def browse_file(self):
        file_name, file_filter = QFileDialog.getOpenFileName(
            self, "Pick a File", "", "All Files (*)")
        if file_name:
            self.log_message("File Picked: " + file_name)

    def saveTo_file(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select Folder to Save", "")
        if folder_path:
            self.log_message("Save File To: " + folder_path)

    def log_message(self, message):
        self.logMessage.append("[LOG] " + message)
        self.logMessage.append(" ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = hestiaMain()
    window.show()
    sys.exit(app.exec())
