import sys
import os
import threading
import qdarktheme
from PIL import Image
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from python_ui import Ui_HestiaConverter
from PyQt6.QtCore import Qt
from moviepy.editor import VideoFileClip


class hestiaMain(QMainWindow, Ui_HestiaConverter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.filename = ""
        self.outputFolder = ""
        self.import_box.setReadOnly(True)

        # Disabled buttons initially
        self.save_button.setEnabled(False)
        self.convert_button.setEnabled(False)

        self.import_button.clicked.connect(self.browse_file)
        self.save_button.clicked.connect(self.saveTo_file)
        self.convert_button.clicked.connect(self.convert_file)

    def log_import(self, message):
        try:
            self.import_box.setText(message)
        except Exception as e:
            print(f"Error logging message: {e}")

    def log_message(self, message):
        # Log the message using the log function
        try:
            self.logMessage.append("[LOG] " + message)
            self.logMessage.append(" ")
        except Exception as e:
            print(f"Error logging message: {e}")

    def browse_file(self):
        try:
            self.file_name, _ = QFileDialog.getOpenFileName(
                self, "Pick a File", "", "Mp4 (*.mp4);;Mp3 (*.mp3);;PNG (*.png);;JPG (*.jpg, *.jpeg);;Webp (*.webp),")

            # Extract file extension
            self.original_extension = os.path.splitext(self.file_name)[1]
            if self.original_extension == ".jpg":
                self.original_extension = ".jpeg"

            if self.original_extension in [self.convert_from_comboBox.itemText(i) for i in range(self.convert_from_comboBox.count())]:
                self.convert_from_comboBox.setCurrentText(
                    self.original_extension)
                self.log_message(
                    f"File Picked: {self.file_name}, File Extension: {self.original_extension}")
                self.log_import(f"{self.file_name}")
                self.save_button.setEnabled(True)
        except Exception as e:
            self.log_message(f"Error browsing file: {e}")

    def saveTo_file(self):
        try:
            folder_path = QFileDialog.getExistingDirectory(
                self, "Select Folder to Save", "")
            if folder_path:
                self.log_message("Save File To: " + folder_path)
                self.convert_button.setEnabled(True)
            self.outputFolder = folder_path
        except Exception as e:
            self.log_message(f"Error saving file: {e}")

    def convert_file(self):
        try:
            convert_From = self.original_extension
            self.log_message(f"Converting from {convert_From}")
            convert_To = self.convert_To_comboBox.currentText()
            self.log_message(f"Converting to {convert_To}")
            inputFile = self.file_name
            output_filename = os.path.basename(
                self.file_name).replace(convert_From, convert_To)
            self.log_message(f"Output File name: {output_filename}")
            output_folder = self.outputFolder
            output_file = f"{output_folder}/{output_filename}"

            self.log_message(f"Output File name: {output_file}")

            self.log_message(f"Converting File....")

            conversion_thread = threading.Thread(
                target=self.perform_conversion, args=(inputFile, output_file, convert_To, convert_From))
            conversion_thread.start()
        except Exception as e:
            self.log_message(f"Error converting file: {e}")

    def perform_conversion(self, input_file, output_file, convert_To, convert_From):
        try:
            if convert_From == ".jpeg":
                convert_From = ".jpg"

            _, file_extension = os.path.splitext(input_file)

            if file_extension == ".jpeg":
                file_extension = ".jpg"

            self.log_message(f"Imported File: {input_file}")
            self.log_message(f"Imported File Extension: {convert_From}")
            self.log_message(f"Output File Extension: {convert_To}")

            if file_extension.lower() == convert_From.lower():
                if file_extension.lower() in [".jpg", ".png", ".webp"]:
                    with Image.open(input_file) as img:
                        if img.mode == 'RGBA':
                            img = img.convert('RGB')
                        elif img.mode != 'RGB':
                            img = img.convert('RGB')

                        # Use convert_To directly instead of converting it to converted_extension
                        img.save(output_file, format=convert_To.upper()[1:])
                        self.log_message(
                            f"Image Conversion successful: {output_file}")
                elif file_extension.lower() == ".mp4":
                    clip = VideoFileClip(input_file)
                    clip.audio.write_audiofile(output_file)
                    self.log_message(
                        f"Video Conversion successful: {output_file}")
                else:
                    self.log_message("Invalid file extension for conversion")
            else:
                self.log_message("File extension mismatch for conversion")
        except Exception as e:
            self.log_message(f"Error performing conversion: {e}")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        qdarktheme.setup_theme()
        window = hestiaMain()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error starting the application: {e}")
