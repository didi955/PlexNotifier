from tmdbv3api import TMDb
from tmdbv3api import Movie
from tmdbv3api import TV
from YMLFiles import Configuration

CONFIGURATION = Configuration(open("config.yml", "r+", encoding='utf-8'))
KEY = CONFIGURATION.getTheMovieDBAPIKey()

tmdb = TMDb()
tmdb.language = 'fr'
tmdb.api_key = KEY

movie = Movie()
tv = TV()


def getShowPoster_URL(title: str):
    search = tv.search(title)
    if search:
        res = search[0]
        return "https://image.tmdb.org/t/p/original/" + res.poster_path
    else:
        return "error"


def getMoviePoster_URL(title: str):
    search = movie.search(title)
    if search:
        res = search[0]
        return "https://image.tmdb.org/t/p/original/" + res.poster_path
    else:
        return "error"
