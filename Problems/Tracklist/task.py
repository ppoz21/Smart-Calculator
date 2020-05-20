def tracklist(**kwargs):
    for key, value in kwargs.items():
        print(key)
        for album, track in value.items():
            print(f"ALBUM: {album} TRACK: {track}")
