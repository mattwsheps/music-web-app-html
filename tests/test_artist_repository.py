from lib.artist_repository import *
from lib.artist import *

"""
When I call get #all
I get a list of all artists in the artists table
"""
def test_list_all_artists(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

"""
When I call #create
I create an artist in the database
And can see it in #all
"""
def test_create_artist(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Wild nothing", "Indie")
    repository.create(artist)
    artists = repository.all()
    assert artists == [
        Artist(1, 'Pixies', 'Indie'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]

"""
When we call #find
We get a single Artist object
"""
def test_find_artist(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = ArtistRepository(db_connection)

    artist = repository.find(1)
    assert artist == Artist(1, "Pixies", "Indie")