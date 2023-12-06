from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all the albums in the albums table
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()
    assert albums == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1)
        ]

"""
When I call #create
I create an album in the database
And I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Album", 2000, 1)
    repository.create(album)
    albums = repository.all()
    assert albums == [
            Album(1, "Doolittle", 1989, 1),
            Album(2, "Surfer Rosa", 1988, 1),
            Album(3, "Test Album", 2000, 1)
        ]

"""
When I call #find with an id
We get that Album data
"""
def test_find_album(db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(2)
    assert album == Album(2, "Surfer Rosa", 1988, 1)