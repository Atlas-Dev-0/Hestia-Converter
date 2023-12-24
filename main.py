import sys
import os
import threading
import qdarktheme
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from python_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip


class hestiaMain(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.filename = ""
        self.outputFolder = ""

        self.import_button.clicked.connect(self.browse_file)
        self.save_button.clicked.connect(self.saveTo_file)
        self.convert_button.clicked.connect(self.convert_file)

    def log_message(self, message):
        self.logMessage.append("[LOG] " + message)
        self.logMessage.append(" ")

    def browse_file(self):
        self.file_name, _ = QFileDialog.getOpenFileName(
            self, "Pick a File", "", "Mp4 (*.mp4);;Mp3 (*.mp3);;PNG (*.png);;JPG (*.jpg);;Webp (*.webp)", )

        if self.file_name:
            # Extract file extension
            fileName_value, file_extension = os.path.splitext(self.file_name)

            if file_extension in [self.convert_from_comboBox.itemText(i) for i in range(self.convert_from_comboBox.count())]:
                self.convert_from_comboBox.setCurrentText(file_extension)

            self.log_message(
                f"File Picked: {fileName_value}, File Extension: {file_extension}")

    def saveTo_file(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select Folder to Save", "")
        if folder_path:
            self.log_message("Save File To: " + folder_path)
        self.outputFolder = folder_path

    def convert_file(self):
        convert_From = self.convert_from_comboBox.currentText()
        convert_To = self.convert_To_comboBox.currentText()
        output_filename = os.path.basename(
            self.file_name).replace(convert_From, convert_To)
        output_folder = self.outputFolder
        output_file = f"{output_folder}/{output_filename}"

        self.log_message(f"Converting File....")

        conversion_thread = threading.Thread(
            target=self.perform_conversion, args=(self.file_name, output_file))
        conversion_thread.start()

    def perform_conversion(self, input_file, output_file):
        
        try:
            if ".png" in input_file:
                
            elif ".jpg" in input_file:
                
            elif ".mp4" in input_file:
                clip = VideoFileClip(input_file)
                clip.audio.write_audiofile(output_file)
                self.log_message(f"Conversion successful: {output_file}")

        except Exception as e:
            self.log_message(f"Error during conversion: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qdarktheme.setup_theme()
    window = hestiaMain()
    window.show()
    sys.exit(app.exec())
