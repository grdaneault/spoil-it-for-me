class Character:
    def __init__(self, name: str, actor: str, episodes: int, image: str):
        self.name = name
        self.actor = actor
        self.episodes = episodes
        self.image = image

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "actor": self.actor
        }
