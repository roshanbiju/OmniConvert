from pathlib import Path

from core.format_registry import (
    get_importer,
    get_exporter
)


class ConversionManager:

    @staticmethod
    def convert(input_file, output_file):

        source_ext = Path(
            input_file
        ).suffix.lower()

        target_ext = Path(
            output_file
        ).suffix.lower()

        importer = get_importer(
            source_ext
        )

        exporter = get_exporter(
            target_ext
        )

        if importer is None:
            raise Exception(
                f"No importer registered for {source_ext}"
            )

        if exporter is None:
            raise Exception(
                f"No exporter registered for {target_ext}"
            )

        model = importer(
            input_file
        )

        exporter(
            model,
            output_file
        )