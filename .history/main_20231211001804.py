from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QVBoxLayout, QProgressBar
import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip
from main_ui import Ui_MainWindow


class ConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browseButton.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.convert_file)
        self.pushButton_2.clicked.connect(self.save_to)

        self.progressBar.setValue(0)  # Set initial value
        self.progressBar.setMaximum(100)  # Set maximum value

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

        try:
            clip = VideoFileClip(input_file)

            # Set up the callback function to update progress bar and log
            def callback_progress(t):
                progress_value = int(t / clip.duration * 100)
                self.progressBar.setValue(progress_value)
                self.log_message(f"Converting: {progress_value}%")

            clip.audio.write_audiofile(
                output_file, progress_bar_callback=callback_progress)

            # clip.audio.write_audiofile(output_file)
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


class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Converting...")
        self.setFixedSize(300, 100)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 30, 260, 30)

        layout = QVBoxLayout(self)
        layout.addWidget(self.progressBar)

        self.setMaximum(100)
        self.setValue(0)

    def setValue(self, value):
        self.progressBar.setValue(value)


class ConverterApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.browseButton.clicked.connect(self.browse_file)
        self.pushButton.clicked.connect(self.convert_file)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select a file", "", "MP4 Files (*.mp4);;All Files (*)")

        if file_name:
            self.filePathLineEdit.setText(file_name)

    def convert_file(self):
        input_file = self.filePathLineEdit.text()

        if not input_file:
            self.log_message("Error: Please select a file.")
            return

        if self.radioButton_3.isChecked():
            output_format = ".mp3"
        elif self.radioButton_2.isChecked():
            output_format = ".wav"
        else:
            self.log_message("Error: Please select an output format.")
            return

        output_file = input_file.replace(".mp4", output_format)

        # Create and show the progress dialog
        progress_dialog = ProgressDialog(self)
        progress_dialog.show()

        try:
            clip = VideoFileClip(input_file)
            total_frames = int(clip.audio.fps * clip.audio.duration)

            for i, _ in enumerate(clip.audio.iter_frames()):
                progress = int((i + 1) / total_frames * 100)
                progress_dialog.setValue(progress)
                QApplication.processEvents()

            clip.audio.write_audiofile(output_file)

            self.log_message(f"Conversion successful: {output_file}")

        except Exception as e:
            self.log_message(f"Error during conversion: {str(e)}")

        finally:
            # Close the progress dialog
            progress_dialog.close()

    def log_message(self, message):
        self.textEdit.append(message)


if __name__ == "__main__":
    app = QApplication([])
    window = ConverterApp()
    window.show()
    app.exec()
