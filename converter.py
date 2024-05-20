import os
from PIL import Image
import argparse

def find_tiff_files(directory):
    tiff_files = [f for f in os.listdir(directory) if f.lower().endswith('.tiff') or f.lower().endswith('.tif')]
    return tiff_files

def convert_image(file_path, output_format):
    image = Image.open(file_path)
    base_name = os.path.splitext(file_path)[0]
    output_file = f"{base_name}.{output_format.lower()}"
    image.save(output_file, format=output_format.upper())
    return output_file

def convert_tiff_files(directory, output_format):
    tiff_files = find_tiff_files(directory)
    if not tiff_files:
        print("No TIFF files found")
        return

    for tiff_file in tiff_files:
        file_path = os.path.join(directory, tiff_file)
        converted_file = convert_image(file_path, output_format)
        print(f"Converted {tiff_file} to {converted_file}")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Convert TIFF to JPEG or PNG")
    parser.add_argument("directory", help="Directory to search for TIFF files")
    parser.add_argument("output_format", choices=["jpeg", "png"], help="choose jpeg or png")
    args = parser.parse_args()

    convert_tiff_files(args.directory, args.output_format)

# os.system command
# subprocess
# take advantage of wildcard/token to detect all files of a type *.tif
# CREATE A UI to use ? match sequence - PYTHON LIB FILE SEQ
