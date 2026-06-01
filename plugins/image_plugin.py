from core.format_registry import (
    register_importer,
    register_exporter
)

from importers.image_importer import (
    import_image
)

from exporters.image_exporter import (
    export_image
)


IMAGE_FORMATS = [
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp",
    ".tiff"
]


for ext in IMAGE_FORMATS:

    register_importer(
        ext,
        import_image
    )

    register_exporter(
        ext,
        export_image
    )