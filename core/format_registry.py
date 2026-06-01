IMPORTERS = {}
EXPORTERS = {}


def register_importer(extension, handler):
    IMPORTERS[extension.lower()] = handler


def register_exporter(extension, handler):
    EXPORTERS[extension.lower()] = handler


def get_importer(extension):
    return IMPORTERS.get(extension.lower())


def get_exporter(extension):
    return EXPORTERS.get(extension.lower())