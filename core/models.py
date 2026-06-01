class UniversalImage:

    def __init__(
        self,
        image,
        metadata=None
    ):
        self.image = image
        self.metadata = metadata or {}