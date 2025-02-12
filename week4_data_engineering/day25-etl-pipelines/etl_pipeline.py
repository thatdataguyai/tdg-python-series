from helper.helper import *

def main():
    # Step 1: Extract
    drake_data = extract_drake_data()
    top_tracks = extract_top_tracks(drake_data['artist_id'])
    albums = extract_albums(drake_data['artist_id'])
    
    # Step 2: Transform
    transformed_artist_data = transform_artist_data(drake_data)
    transformed_tracks = [transform_track_data(track) for track in top_tracks]
    transformed_albums = [transform_album_data(album) for album in albums]
    
    # Step 3: Load
    load_artist_data(transformed_artist_data)
    for album in transformed_albums:
        load_album_data(album)
    for track in transformed_tracks:
        load_track_data(track)
    
    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()