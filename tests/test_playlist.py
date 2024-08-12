from lib.playlist import *

def test_playlist():

    playlist = Playlist()

    playlist.add("Blues")
    playlist.add("Jazz")
    playlist.add("Reggae")

    assert playlist.listtracks() == ["Blues", "Jazz", "Reggae"]