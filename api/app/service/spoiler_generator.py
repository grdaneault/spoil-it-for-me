from app.model import Media, Spoiler
import random
from jinja2 import Template


class SpoilerTemplate:
    def __init__(self, template: str):
        self.template = Template(template)

    def apply(self, context):
        msg = self.template.render(ctx=context)
        return Spoiler(media=context.media, message=msg, background_image="https://timedotcom.files.wordpress.com/2019/05/game-of-thrones-season-8-episode-5-davos-jon-snow.jpg")


class SpoilerContext:
    def __init__(self, media: Media):
        self.media = media

    @property
    def character(self):
        return random.choice(self.media.characters).name

class SpoilerGenerator:
    TEMPLATES = [
        SpoilerTemplate("{{ctx.character}} dies in the end."),
        SpoilerTemplate("{setting} is in an alternate dimension."),
        SpoilerTemplate("{{ctx.character}} was dead the whole time."),
        SpoilerTemplate("{{ctx.character}} was actually {{ctx.character}} in disguise."),
        SpoilerTemplate("<strong>{{ctx.character}}</strong> makes it out alive.")
    ]

    def generate(self, media: Media):
        context = SpoilerContext(media=media)
        return random.choice(SpoilerGenerator.TEMPLATES).apply(context)