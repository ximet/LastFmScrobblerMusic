# for using install PyObjC: bridge between the Python and Objective-C
import ScriptingBridge
import parser
import lastfm

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
        self.connection_to_apple_music()


    def connection_to_apple_music(self):
        self.a_music = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
        print("Connection to Apple Music: correct")



scrobbler = Scrobbler('config.json')
