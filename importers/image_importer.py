from PIL import Image

from core.models import UniversalImage


def import_image(path):

    image = Image.open(path)

    return UniversalImage(image)