import parser
import lastfm
import amusic

class Scrobbler(object):
    a_music = None
    lastfm = None
    config = None

    def __init__(self, filename):
        self.filename = filename
        self.confugure_connect_to_service()

    def confugure_connect_to_service(self):
        self.config = parser.parse_json(self.filename)
        self.lastfm = lastfm.connection_to_lastfm(self.config)
        self.a_music = amusic.connection_to_apple_music()


scrobbler = Scrobbler('config.json')
