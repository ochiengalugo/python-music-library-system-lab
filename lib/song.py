class Song:
    # Class attributes to track global state
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        # Initialize instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger tracking updates automatically upon new song creation
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        """Increments the total value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        """Adds new genres to a class attribute genres list. Ensures unique values."""
        # We look at the last created song instance's genre, or pass it via context if needed.
        # In a standard lab setup triggering inside __init__, we safely reference the current state.
        pass 

    @classmethod
    def add_to_artists(cls):
        """Adds new artists to a class attribute artists list. Ensures unique values."""
        pass

    # Alternative implementation to make the automatic triggers elegant:
    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Updates class attribute genre_count dictionary tracking."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists_count(self):
        """Updates class attribute artists_count dictionary tracking."""
        if self.artist in Song.artists_count:
            Song.artists_count[self.artist] += 1
        else:
            Song.artists_count[self.artist] = 1
