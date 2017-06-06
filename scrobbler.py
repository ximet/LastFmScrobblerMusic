import pylast
import json
import ScriptingBridge

class Scrobbler(object):
    a_music = None
    lastfm = None
    config = None

    def __init__(self, filename):
        self.filename = filename
        self.parse_json(self.filename)
        self.connection_to_lastfm()
        self.connection_to_apple_music()

    def parse_json(self, filename):
        with open(filename) as data_file:
            self.config = json.load(data_file)

    def connection_to_lastfm(self):
        API_KEY = self.config["API_KEY"]
        API_SECRET = self.config["API_SECRET"]
        username = self.config["username"]
        password = pylast.md5(self.config["password"])
        self.lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password)
        print("Connection to LastFM: correct")

    def connection_to_apple_music(self):
        self.a_music = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
        print("Connection to Apple Music: correct")




scrobbler = Scrobbler('config.json')
