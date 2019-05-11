from flask import jsonify, abort

from app import app
from app.media import MEDIA
from app.service import SpoilerGenerator


@app.route('/api/media')
def media_list():
    return jsonify([m.to_json() for m in MEDIA])


@app.route('/api/media/<int:id>/spoiler')
def spoil_it(id: int):
    media = [m for m in MEDIA if m.id == id]
    if not media:
        return abort(404)
    media = media[0]
    gen = SpoilerGenerator()
    return jsonify(gen.generate(media).to_json())
