class SearcherShows:

    def __init__(self, library):
        """Constructor that creates a Searcher instance.

        :param library: The library to search in.
        """
        self.library = library

    def searchUnwatchedEpisodes(self):
        ls = []
        for episode in self.library.search(unwatched=True, libtype='episode'):
            ls.append(episode)

        return ls

    def searchUnwatchedSeasons(self):
        ls = []
        for season in self.library.search(unwatched=True, libtype='season'):
            ls.append(season)

        return ls

    def searchUnwatchedShows(self):
        ls = []
        for show in self.library.search(unwatched=True, libtype='show'):
            ls.append(show)

        return ls


class SearcherMovies:

    def __init__(self, library):
        self.library = library

    def searchUnwatchedMovies(self):
        ls = []
        for movie in self.library.search(unwatched=True, libtype='movie'):
            ls.append(movie)

        return ls
