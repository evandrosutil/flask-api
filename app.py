import os
import uuid

import requests

from flask import Flask, request
from flask_caching import Cache

from aws_controller import create_song_list


GENIUS_URL = 'http://api.genius.com/search?q={}'
GENIUS_ACCESS_TOKEN = os.environ.get('GENIUS_ACCESS_TOKEN', '')

app = Flask(__name__)
app.config.from_object('config.Config')

cache = Cache(app)


@app.route("/artist")
def get_musics():
    headers = {'Authorization':  GENIUS_ACCESS_TOKEN}

    artist = request.args.get('artist', None)
    cache_result = request.args.get('cache', True)
    if cache_result == 'False':
        cache_result = False

    artist_info = cache.get(artist)
    if not artist_info:
        app.logger.info('Consultando %s na API do Genius.', artist)
        response = requests.get(GENIUS_URL.format(artist), headers=headers)
        songs_list = response.json()['response']['hits']
        top_songs = [song['result'].get('title') for song in songs_list]
        transaction_uuid = str(uuid.uuid4())
        artist_info = {
            'artist': artist,
            'top_songs': top_songs,
            'uuid': transaction_uuid
        }
    if not cache_result:
        app.logger.info("Deletando informação do cache")
        try:
            create_song_list(
                artist, artist_info['top_songs'], artist_info['uuid']
            )
        except ValueError:
            app.logger.info("Artista já existente.")
        cache.delete(artist)
    else:
        cache.set(
            artist, {
                'top_songs': artist_info['top_songs'],
                'uuid': artist_info['uuid']
            }
        )

    return {'artist': artist, 'top_songs': artist_info['top_songs']}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
