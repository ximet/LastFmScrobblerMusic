import pylast

class Scrobbler(object):
    a_music = None
    lastfm = None

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg

    def setup_lastfm(arg):
        API_KEY = ""
        API_SECRET = ""
        username = ""
        password = pylast.md5("")
        self.lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
