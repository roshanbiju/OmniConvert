from PIL import Image


class ImageConverter:

    @staticmethod
    def convert(
        input_file,
        output_file
    ):

        image = Image.open(
            input_file
        )

        if output_file.lower().endswith(".jpg"):
            image = image.convert("RGB")

        image.save(
            output_file
        )