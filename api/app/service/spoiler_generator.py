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
            background_image=random.choice(context.potential_images))


class SpoilerContext:
    def __init__(self, media: Media):
        self.media = media
        self.potential_images = []

    @property
    def character(self):
        character = random.choice(self.media.characters)
        self.potential_images.append(character.image)
        return character.name

    @property
    def setting(self):
        setting = random.choice(self.media.settings)
        self.potential_images.append(setting.image)
        return setting.name


class SpoilerGenerator:
    TEMPLATES = [
        "{{ctx.character}} dies in the end.",
        "{{ctx.setting}} is in an alternate dimension.",
        "{{ctx.character}} was dead the whole time.",
        "{{ctx.character}} was actually {{ctx.character}} in disguise.",
        "{{ctx.character}} makes it out alive.",
        "{{ctx.character}} is betrayed by {{ctx.character}}",
        "{{ctx.setting}} burns to the ground",
        "{{ctx.setting}} is returned to glory"
    ]

    def generate(self, media: Media):
        context = SpoilerContext(media=media)
        template = random.choice(SpoilerGenerator.TEMPLATES + media.custom_spoilers)
        return SpoilerTemplate(template).apply(context)
