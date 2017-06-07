# for using install PyObjC: bridge between the Python and Objective-C
import ScriptingBridge

def connection_to_apple_music():
    a_music = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
    print("Connection to Apple Music: correct")
    return a_music

def which_music_playing_now(instance):
    current_track = instance.currentTrack()
    object_song = {
            'artist': current_track.artist(),
            'title': current_track.name(),
            'album': current_track.album(),
            'album_artist': current_track.albumArtist(),
            'track_number': current_track.trackNumber(),
            'duration': int(current_track.duration())
        }
    print(object_song) #for logging
    return object_song
