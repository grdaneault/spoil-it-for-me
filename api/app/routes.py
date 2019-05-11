from flask import jsonify

from app import app


@app.route('/media')
def media_list():
    return jsonify([{
        "id": 1,
        "title": "Avengers: Endgame",
        "type": "movie"
    }, {
        "id": 2,
        "title": "Game of Thrones",
        "type": "tv"
    }])

@app.route('/media/{id}/spoiler')
def spoil_it(id):
    return jsonify({
        "media": {
            "this_is_where_the_media_object_would_go": True
        },
        "message": "this is where I'd put a spoiler... if I had one!",
        "background_image": "https://imgflip.com/s/meme/This-Is-Where-Id-Put-My-Trophy-If-I-Had-One.jpg"
    })

