import pylast

def connection_to_lastfm(config):
    API_KEY = config["API_KEY"]
    API_SECRET = config["API_SECRET"]
    username = config["username"]
    password = pylast.md5(config["password"])
    lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                           username=username, password_hash=password)
    print("Connection to LastFM: correct")
    return lastfm
