from app.model import Media, Spoiler
import random

class SpoilerTemplate:
    TAG_PERSON = "%PERSON%"
    TAG_PLACE = "%PLACE%"

    def __init__(self, template: str):
        self.template = template

    def apply(self, context):
        msg = self.template.replace(SpoilerTemplate.TAG_PERSON, context.get_person())
        return Spoiler(media=context.media, message=msg, background_image="https://cnet2.cbsistatic.com/img/x7wuV8zJXZqcLlS69HizMkSYYv0=/940x0/2019/04/02/0f0b1a02-e399-4c62-b409-c92a2b1904d2/reald3d.jpg")

class SpoilerContext:
    def __init__(self, media: Media):
        self.media = media

    def get_person(self):
        return "A character"



class SpoilerGenerator:
    TEMPLATES = [
        SpoilerTemplate("{character} dies in the end."),
        SpoilerTemplate("{setting} is in an alternate dimension."),
        SpoilerTemplate("{character} was dead the whole time."),
        SpoilerTemplate("{character} was actually {character}")
    ]

    def generate(self, media: Media):
        context = SpoilerContext(media=media)
        return random.choice(SpoilerGenerator.TEMPLATES).apply(context)