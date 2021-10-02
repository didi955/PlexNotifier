from tmdbv3api import Movie
from tmdbv3api import TMDb
from tmdbv3api import TV

from YMLFiles import Configuration


def init(configPath):
    config = Configuration(open(configPath, "r+", encoding='utf-8'))
    key = config.getTheMovieDBAPIKey()

    tmdb = TMDb()
    tmdb.language = 'fr'
    tmdb.api_key = key


def getShowPoster_URL(title: str):
    tv = TV()
    search = tv.search(title)
    if search:
        res = search[0]
        return "https://image.tmdb.org/t/p/original/" + res.poster_path
    else:
        return "error"


def getMoviePoster_URL(title: str):
    movie = Movie()
    search = movie.search(title)
    if search:
        res = search[0]
        return "https://image.tmdb.org/t/p/original/" + res.poster_path
    else:
        return "error"
