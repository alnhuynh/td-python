import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PIL import Image
import fileseq

def find_files(directory, pattern):
    # Parse the input pattern to handle file sequences
    sequence = fileseq.findSequencesOnDisk(os.path.join(directory, pattern))
    files = [f for seq in sequence for f in seq]
    return files

def convert_image(file_path, output_format):
    image = Image.open(file_path)
    base_name = os.path.splitext(file_path)[0]
    output_file = f"{base_name}.{output_format.lower()}"

    # OSError: cannot write mode RGBA as JPEG
    if output_format.lower() == 'jpeg' and image.mode == 'RGBA':
        # Convert RGBA to RGB for JPEG
        image = image.convert('RGB')

    image.save(output_file, format=output_format.upper())
    return output_file

def convert_files(directory, pattern, output_format):
    files = find_files(directory, pattern)
    if not files:
        print("No matching files found")
        return

    for file in files:
        file_path = os.path.join(directory, file)
        converted_file = convert_image(file_path, output_format)
        print(f"Converted {file} to {converted_file}")

class FileSearchUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.directory = None

        self.directory_label = QLabel('Directory:', self)
        self.directory_input = QLineEdit(self)
        self.browse_button = QPushButton('Browse', self)
        self.browse_button.clicked.connect(self.browseDirectory)

        self.pattern_label = QLabel('File Pattern:', self)
        self.pattern_input = QLineEdit(self)

        self.type_label = QLabel('File Type:', self)
        self.type_dropdown = QComboBox(self)
        self.type_dropdown.addItems(["jpeg", "png", "tiff"])

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.onSubmit)

        layout = QVBoxLayout()

        directory_layout = QHBoxLayout()
        directory_layout.addWidget(self.directory_label)
        directory_layout.addWidget(self.directory_input)
        directory_layout.addWidget(self.browse_button)

        pattern_layout = QHBoxLayout()
        pattern_layout.addWidget(self.pattern_label)
        pattern_layout.addWidget(self.pattern_input)

        type_layout = QHBoxLayout()
        type_layout.addWidget(self.type_label)
        type_layout.addWidget(self.type_dropdown)

        layout.addLayout(directory_layout)
        layout.addLayout(pattern_layout)
        layout.addLayout(type_layout)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        self.setWindowTitle('File Search and Convert')
        self.show()

    def browseDirectory(self):
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if self.directory:
            self.directory_input.setText(self.directory)

    def onSubmit(self):
        pattern = self.pattern_input.text()
        file_type = self.type_dropdown.currentText()
        directory = self.directory_input.text()
        
        if not directory:
            print("Please select a directory")
            return
        
        print(f'Searching for files matching pattern: {pattern} in directory: {directory} of type: {file_type}')
        convert_files(directory, pattern, file_type)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileSearchUI()
    sys.exit(app.exec_())
