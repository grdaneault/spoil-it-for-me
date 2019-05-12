from app.model import Character
from app.model import Setting

from typing import List


class Media:
    def __init__(self, media_id: int, title: str, media_type: str, characters: List[Character], settings: List[Setting],
                 custom_spoilers: List[str], images: List[str]):
        self.id = media_id
        self.title = title
        self.type = media_type
        self.characters = []
        self.settings = settings
        self.custom_spoilers = custom_spoilers
        self.images = images

        if media_type == 'tv':
            # Weight characters by number of episodes
            for c in characters:
                for i in range(c.episodes // 10):
                    self.characters.append(c)
        else:
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
