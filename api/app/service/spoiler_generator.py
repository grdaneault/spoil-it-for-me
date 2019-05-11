from app.model import Media, Spoiler
import random
from jinja2 import Template


class SpoilerTemplate:
    def __init__(self, template: str):
        self.template = Template(template)

    def apply(self, context):
        msg = self.template.render(ctx=context)
        return Spoiler(
            media=context.media,
            message=msg,
            background_image=random.choice(context.media.images))


class SpoilerContext:
    def __init__(self, media: Media):
        self.media = media

    @property
    def character(self):
        return random.choice(self.media.characters).name

    @property
    def setting(self):
        return random.choice(self.media.settings)

class SpoilerGenerator:
    TEMPLATES = [
        "{{ctx.character}} dies in the end.",
        "{{ctx.setting}} is in an alternate dimension.",
        "{{ctx.character}} was dead the whole time.",
        "{{ctx.character}} was actually {{ctx.character}} in disguise.",
        "{{ctx.character}} makes it out alive."
    ]

    def generate(self, media: Media):
        context = SpoilerContext(media=media)
        template = random.choice(SpoilerGenerator.TEMPLATES + media.custom_spoilers)
        return SpoilerTemplate(template).apply(context)
