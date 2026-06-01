class UniversalImage:
    def __init__(
        self,
        image,
        metadata=None
    ):
        self.image = image
        self.metadata = metadata or {}


class UniversalAudio:
    def __init__(
        self,
        samples=None,
        metadata=None
    ):
        self.samples = samples
        self.metadata = metadata or {}


class UniversalDocument:
    def __init__(
        self,
        content="",
        metadata=None
    ):
        self.content = content
        self.metadata = metadata or {}