import pylast

SCROBBLE_ATTEMPTS = 3

def connection_to_lastfm(config):
    API_KEY = config["API_KEY"]
    API_SECRET = config["API_SECRET"]
    username = config["username"]
    password = pylast.md5(config["password"])
    lastfm = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                           username=username, password_hash=password)
    print("Connection to LastFM: correct")
    return lastfm

def scrobbling_music(instance, music):
    for attempt in range(SCROBBLE_ATTEMPTS):
        try:
            instance.scrobble(**music)
            print('scrobbling correct') #for logging
            break
        except pylast.WSError:
            time.sleep(15)
    else:
        print('have problem with scrobbling this song') #for logging
