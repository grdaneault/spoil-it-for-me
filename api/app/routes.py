from flask import jsonify, abort

from app import app
from app.model import Media
from app.service import SpoilerGenerator

MEDIA = [
    Media(media_id=1, title="Avengers: Endgame", media_type="movie"),
    Media(media_id=2, title="Game of Thrones", media_type="tv"),
    Media(media_id=3, title="Harry Potter", media_type="movie"),
    Media(media_id=4, title="Detective Pikachu", media_type="movie"),
    Media(media_id=5, title="Mr. Robot", media_type="tv"),
]

@app.route('/media')
def media_list():
    return jsonify([m.to_json() for m in MEDIA])

@app.route('/media/<int:id>/spoiler')
def spoil_it(id):
    media = [m for m in MEDIA if m.id == id]
    if not media:
        return abort(404)
    media = media[0]
    gen = SpoilerGenerator()
    return jsonify(gen.generate(media).to_json())

