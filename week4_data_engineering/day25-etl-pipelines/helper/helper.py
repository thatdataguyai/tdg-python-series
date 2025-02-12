import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Extract Data
# Spotify API credentials
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # Must match your Spotify app settings

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope='user-library-read'
))

# Fetch Drake's artist data
def extract_drake_data():
    # Search for Drake
    results = sp.search(q='artist:Drake', type='artist', limit=1)
    drake = results['artists']['items'][0]
    return {
        'artist_id': drake['id'],
        'name': drake['name'],
        'genres': ', '.join(drake['genres']),
        'popularity': drake['popularity'],
        'followers': drake['followers']['total']
    }

# Fetch Drake's top tracks
def extract_top_tracks(artist_id):
    results = sp.artist_top_tracks(artist_id)
    return [{
        'track_id': track['id'],
        'name': track['name'],
        'duration_ms': track['duration_ms'],
        'explicit': track['explicit'],
        'popularity': track['popularity'],
        'album_id': track['album']['id']
    } for track in results['tracks']]

# Fetch Drake's albums
def extract_albums(artist_id):
    results = sp.artist_albums(artist_id, album_type='album', limit=10)
    return [{
        'album_id': album['id'],
        'name': album['name'],
        'release_date': album['release_date'],
        'total_tracks': album['total_tracks']
    } for album in results['items']]


# Transform Data
def transform_artist_data(artist_data):
    return (
        artist_data['artist_id'],
        artist_data['name'],
        artist_data['genres'],
        artist_data['popularity'],
        artist_data['followers']
    )

def transform_track_data(track_data):
    return (
        track_data['track_id'],
        track_data['name'],
        track_data['duration_ms'],
        track_data['explicit'],
        track_data['popularity'],
        track_data['album_id']
    )

def transform_album_data(album_data):
    return (
        album_data['album_id'],
        album_data['name'],
        album_data['release_date'],
        album_data['total_tracks']
    )


# Load Data into SQLite
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('drake.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Artists (
        artist_id TEXT PRIMARY KEY,
        name TEXT,
        genres TEXT,
        popularity INTEGER,
        followers INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Albums (
        album_id TEXT PRIMARY KEY,
        name TEXT,
        release_date TEXT,
        total_tracks INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tracks (
        track_id TEXT PRIMARY KEY,
        name TEXT,
        duration_ms INTEGER,
        explicit BOOLEAN,
        popularity INTEGER,
        album_id TEXT,
        FOREIGN KEY (album_id) REFERENCES Albums(album_id)
    )
''')

# Load artist data
def load_artist_data(artist_data):
    cursor.execute('''
        INSERT OR IGNORE INTO Artists (artist_id, name, genres, popularity, followers)
        VALUES (?, ?, ?, ?, ?)
    ''', artist_data)
    conn.commit()

# Load album data
def load_album_data(album_data):
    cursor.execute('''
        INSERT OR IGNORE INTO Albums (album_id, name, release_date, total_tracks)
        VALUES (?, ?, ?, ?)
    ''', album_data)
    conn.commit()

# Load track data
def load_track_data(track_data):
    cursor.execute('''
        INSERT OR IGNORE INTO Tracks (track_id, name, duration_ms, explicit, popularity, album_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', track_data)
    conn.commit()