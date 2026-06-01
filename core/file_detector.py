from pathlib import Path


def get_extension(filepath):
    return Path(filepath).suffix.lower()