from PIL import Image


def convert(input_file):
    convert_to = "png"  # Use lowercase format
    output_file = "converted.png"
    with Image.open(input_file) as img:
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Convert to uppercase before passing to save
        img.save(output_file, format=convert_to.upper())


input_file = (r'17.JPG')
convert(input_file)
