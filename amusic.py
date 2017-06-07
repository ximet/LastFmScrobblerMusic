# for using install PyObjC: bridge between the Python and Objective-C
import ScriptingBridge

def connection_to_apple_music():
    a_music = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
    print("Connection to Apple Music: correct")
    return a_music
