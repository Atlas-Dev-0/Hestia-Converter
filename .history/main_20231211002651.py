import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip
from main_ui import Ui_MainWindow


class ConverterThread(QThread):
    progress_signal = pyqtSignal(float)

    def __init__(self, input_file, output_file, parent=None):
        super().__init__(parent)
        self.input_file = input_file
        self.output_file = output_file

    def run(self):
        try:
            clip = VideoFileClip(self.input_file)

            def progress_callback(progress):
                self.progress_signal.emit(progress)

            clip.audio.write_audiofile(
                self.output_file, progress_callback=progress_callback)

        except Exception as e:
            self.error_message = str(e)
            self.progress_signal.emit(-1)


class ConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browseButton.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.convert_file)
        self.pushButton_2.clicked.connect(self.save_to)

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
        input_file = self.filePathLineEdit.text()

        if self.radioButton_3.isChecked():
            output_format = ".mp3"
        elif self.radioButton_2.isChecked():
            output_format = ".wav"
        else:
            self.log_message("Error: Please Select a Conversion Type.")

        if not input_file:
            self.log_message("Error: Please select a file.")
            return

        output_filename = os.path.basename(
            input_file).replace(".mp4", output_format)
        output_folder = self.filePathLineEdit_3.text()
        output_file = f"{output_folder}/{output_filename}"

        self.log_message(f"Input: {input_file}")

        # try:
        #     clip = VideoFileClip(input_file)
        #     self.log_message(f"Converting File: {input_file}")
        #     clip.audio.write_audiofile(output_file)
        #     self.log_message(f"Conversion successful: {output_file}")

        try:
            def progress_callback(progress):
                # progress is a float between 0 and 1
                progress_percent = int(progress * 100)
                self.log_message(f"Conversion Progress: {progress_percent}%")

            clip = VideoFileClip(input_file)
            self.log_message(f"Converting File: {input_file}")

            clip.audio.write_audiofile(
                output_file, progress_callback=progress_callback)

            self.log_message(f"Conversion successful: {output_file}")

        except Exception as e:
            self.log_message(f"Error during conversion: {str(e)}")

    def log_message(self, message):
        self.textEdit.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())
