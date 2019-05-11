class Media:
    def __init__(self, media_id: int, title: str, media_type: str):
        self.id = media_id
        self.title = title
        self.type = media_type

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "type": self.type
        }
