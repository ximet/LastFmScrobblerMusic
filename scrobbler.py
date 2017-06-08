import parser
import lastfm
import amusic
import time

class Scrobbler(object):
    a_music = None
    lastfm = None
    config = None

    def __init__(self, filename):
        self.filename = filename
        self.confugure_connect_to_service()
        self.scrobbler()

    def confugure_connect_to_service(self):
        self.config = parser.parse_json(self.filename)
        self.lastfm = lastfm.connection_to_lastfm(self.config)
        self.a_music = amusic.connection_to_apple_music()

    def scrobbler(self):
        current_music = amusic.which_music_playing_now(self.a_music);
        current_music['timestamp'] = int(time.time() - self.a_music.playerPosition())
        lastfm.scrobbling_music(self.lastfm, current_music)

scrobbler = Scrobbler('config.json')
