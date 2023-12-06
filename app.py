import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.artist_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    artist_repo = ArtistRepository(connection)
    album = album_repo.find(id)
    artist = artist_repo.find(album.artist_id)
    return render_template('albums/find.html', album=album, artist=artist)

@app.route("/artists", methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artists = artist_repo.all()
    return render_template("artists/index.html", artists=artists)

@app.route("/artists/<int:id>", methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    artist_repo = ArtistRepository(connection)
    artist = artist_repo.find(id)
    return render_template("artists/find.html", artist=artist)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
