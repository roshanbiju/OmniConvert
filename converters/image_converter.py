from PIL import Image


class ImageConverter:

    @staticmethod
    def convert(input_file, output_file):
        image = Image.open(input_file)
        image.save(output_file)