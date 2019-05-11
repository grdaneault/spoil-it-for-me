from app.model import Media


class Spoiler:
    def __init__(self, media: Media, message: str, background_image: str):
        self.media = media
        self.message = message
        self.background_image = background_image

    def to_json(self):
        return {
            "media": self.media.to_json(),
            "message": self.message,
            "background_image": self.background_image
        }
