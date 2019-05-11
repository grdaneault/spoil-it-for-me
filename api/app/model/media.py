from app.model import Character
from typing import List


class Media:
    def __init__(self, media_id: int, title: str, media_type: str, characters: List[Character]):
        self.id = media_id
        self.title = title
        self.type = media_type
        self.characters = characters

    def to_json(self, include_characters=False) -> dict:
        ret = {
            "id": self.id,
            "title": self.title,
            "type": self.type
        }

        if include_characters:
            ret["characters"] = [c.to_json() for c in self.characters]

        return ret
