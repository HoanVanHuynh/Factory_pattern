import json
import xml.etree.ElementTree as et 
# Imagine an application that needs to convert a Song object 
# into its string representation using a specified format.
# Converting an object to a different respresentation is often called serializing.
# You'll often see these requirements implemented in a single function or method
# that contains all the logic and implementation, like in the following code:

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id 
        self.title = title 
        self.artist = artist 

class SongSerializer:
    
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            } 
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)

# In the example above, you have a basic Song class to represent a song
# and a SongSerializer class that can convert a song object into its string representation
# according to the value of the format parameter.
# The .serialize() method supports two different formats: JSON and XML.
# Any other format specified is not supported, so a ValueError exception is raised.
# Let's use the Python interactive shell to see how hte code works:

# This example is short and simplified, but it still has a lot of complexity.
# There are there logical or executin paths depending on the value of the format parameter.
# This may not seem like a big deal, 
# and you've probably seen code with more complexity than this, 
# but the above example is still pretty hard to maintain.
