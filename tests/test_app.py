from playwright.sync_api import Page, expect

"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa"
    ])
    expect(paragraph_tags).to_have_text([
        "Released: 1989",
        "Released: 1988"
    ])

"""
When I call GET /albums/1
I get the first album in the list
"""
def test_get_albums_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tags).to_have_text("Doolittle")
    expect(paragraph_tag).to_have_text([
        "Release year: 1989",
        "Artist: Pixies"
    ])

"""
When I call GET /albums/2
I get the first album in the list
"""
def test_get_albums_2(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    header_1_tags = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(header_1_tags).to_have_text("Surfer Rosa")
    expect(paragraph_tag).to_have_text([
        "Release year: 1988",
        "Artist: Pixies"
    ])

"""
When I call GET /artists
I get a list of artists back
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    list_tags = page.locator("li")
    expect(list_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

"""
When I call GET /artists/1
I get the first artist in the list
"""
def test_get_artists_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tags = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tags).to_have_text("Pixies")
    expect(paragraph_tag).to_have_text("Genre: Indie")

"""
When I call GET /artists/3
I get the first artist in the list
"""
def test_get_artists_3(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists/3")
    h1_tags = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tags).to_have_text("Taylor Swift")
    expect(paragraph_tag).to_have_text("Genre: Pop")