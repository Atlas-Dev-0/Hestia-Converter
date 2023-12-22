import sys
import os
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QTimer
from moviepy.editor import VideoFileClip
from main_ui import Ui_MainWindow


class ConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browseButton.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.convert_file)
        self.pushButton_2.clicked.connect(self.save_to)

        self.conversion_thread = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

    def log_message(self, message):
        self.textEdit.append(message)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Pick an mp4 file", "", "MP4 Files (*.mp4);;All Files (*)")
        if file_name:
            self.filePathLineEdit.setText(file_name)

    def save_to(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "Select Folder to Save", "")
        if folder_path:
            self.filePathLineEdit_3.setText(folder_path)

    def convert_file(self):
        if self.conversion_thread and self.conversion_thread.is_alive():
            self.log_message("Conversion is already in progress.")
            return

        input_file = self.filePathLineEdit.text()

        if self.radioButton_3.isChecked():
            output_format = ".mp3"
        elif self.radioButton_2.isChecked():
            output_format = ".wav"
        else:
            self.log_message("Error: Please Select a Conversion Type.")
            return

        if not input_file:
            self.log_message("Error: Please select a file.")
            return

        output_filename = os.path.basename(
            input_file).replace(".mp4", output_format)
        output_folder = self.filePathLineEdit_3.text()
        output_file = f"{output_folder}/{output_filename}"

        self.log_message(f"Input: {input_file}")

        self.progress_bar.setValue(0)  # Reset progress bar
        self.progress_bar.show()
        self.timer.start(100)  # Update progress every 100 milliseconds

        # Start a new thread for conversion
        self.conversion_thread = threading.Thread(
            target=self.perform_conversion, args=(input_file, output_file))
        self.conversion_thread.start()

    def perform_conversion(self, input_file, output_file):
        try:
            clip = VideoFileClip(input_file)
            total_frames = int(clip.fps * clip.duration)
            for i, frame in enumerate(clip.iter_frames(), start=1):
                # Simulate conversion progress
                progress_percentage = int((i / total_frames) * 100)
                self.progress_bar.setValue(progress_percentage)

            clip.audio.write_audiofile(output_file)
            self.log_message(f"Conversion successful: {output_file}")

        except Exception as e:
            self.log_message(f"Error during conversion: {str(e)}")

    def update_progress(self):
        if self.conversion_thread and not self.conversion_thread.is_alive():
            self.progress_bar.hide()
            self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())
