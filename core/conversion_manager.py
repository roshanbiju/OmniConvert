from importers.image_importer import import_image
from exporters.image_exporter import export_image


class ConversionManager:

    @staticmethod
    def convert(
        input_file,
        output_file
    ):

        model = import_image(
            input_file
        )

        export_image(
            model,
            output_file
        )