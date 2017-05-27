import pylast
import json

class Scrobbler(object):
    a_music = None
    lastfm = None
    config = None

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def parse_json(filename):
        with open(filename) as data_file:
            config = json.load(data_file)

    def setup_lastfm(arg):
        API_KEY = self.config["API_KEY"]
        API_SECRET = self.config["API_SECRET"]
        username = self.config["username"]
        password = pylast.md5(self.config["password"])
        self.lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password)
