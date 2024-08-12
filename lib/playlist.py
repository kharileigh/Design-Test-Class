class Playlist():

    def __init__(self):
        self.tracklist = []
    

    def add(self, str):

        self.tracklist.append(str)
    

    def listtracks(self):

        return self.tracklist