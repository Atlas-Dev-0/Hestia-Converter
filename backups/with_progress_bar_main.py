import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressDialog
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip
from main_ui import Ui_MainWindow


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
        output_format = ".mp3" if self.radioButton_3.isChecked() else ".wav"

        if not input_file:
            self.log_message("Error: Please select a file.")
            return

        output_file = input_file.replace(".mp4", output_format)

        try:
            clip = VideoFileClip(input_file)
            duration = clip.duration  # get the duration of the video
            fps = clip.fps if clip.fps else 30  # use a default fps if not available
            # calculate the number of frames
            frames = int(duration * fps) if duration > 0 else 0

            self.log_message(f"Video fps: {fps} | Video duration: {duration}")

            # Check if there are frames to process
            if frames <= 0:
                self.log_message(
                    "Error: The video file does not contain frames.")
                return

            # create a progress dialog
            progress = QProgressDialog(
                "Converting file...", "Abort", 0, frames, self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)

            if not clip.audio:
                self.log_message(
                    "Error: The video file does not contain any audio.")
                return

            subclip.write_audiofile(output_file, fps=fps)

            for i in range(frames):
                try:
                    # create a subclip of the audio clip
                    subclip = clip.audio.subclip(i / fps, (i + 1) / fps)
                    # write the subclip to a file
                    progress.setValue(i)

                    if progress.wasCanceled():
                        break
                except Exception as subclip_error:
                    # handle errors related to subclip creation or writing
                    self.log_message(
                        f"Error processing subclip {i}: {str(subclip_error)}")

            progress.setValue(frames)
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
