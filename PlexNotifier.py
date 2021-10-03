import time

from plexapi.video import Video

from Mail import *
from PlexInstance import PlexInstance
from Seacher import SearcherMovies
from Seacher import SearcherShows
from YMLFiles import Configuration
from YMLFiles import Data


class PlexNotifier:

    @staticmethod
    def generateId(video: Video):
        return str(video.ratingKey)

    def __init__(self, data: Data, config: Configuration, name: str, ip: str, port: int, token: str):
        self.config = config
        self.plexinstance = PlexInstance(name, ip, port, token)
        self.data = data
        self.mail = Mail(self.config.getSMTPHost(), self.config.getSMTPPort(),
                         self.config.getSMTPMail(), self.config.getSMTPPassword())
        self.new_episodes = None
        self.new_movies = None
        self.searcher_shows = None
        self.searcher_movies = None
        self.shows = None
        self.movies = None

    def init(self):
        self.shows = self.plexinstance.plex.library.section(self.config.getNameShowsCategory())
        self.movies = self.plexinstance.plex.library.section(self.config.getNameMoviesCategory())
        self.searcher_shows = SearcherShows(self.shows)
        self.searcher_movies = SearcherMovies(self.movies)
        MovieDB.init(self.config.file.name)
        self.runTask()

    def runTask(self):
        i = 0
        currentTime = time.time()
        while True:
            if i == 0:
                i = 1
                self.searchNewEpisodes()
                self.searchNewMovies()
            elif time.time() - currentTime > self.config.getIntervalSeconds():
                self.searchNewEpisodes()
                self.searchNewMovies()
                currentTime = time.time()

    def searchNewEpisodes(self):
        self.new_episodes = self.searcher_shows.searchUnwatchedEpisodes()
        for episode in self.new_episodes:
            id = self.generateId(episode)
            self.data.putNewEpisode(id, False)
            if self.data.getNewEpisodeAlertStatus(id) is False:
                self.mail.sendmail(self.config.getEmails(),
                                   "[Plex] Un nouvel épisode est disponible !",
                                   self.mail.getMailNewEpisodeText(episode),
                                   self.mail.getMailNewEpisodeHTML(episode))

                self.data.setNewEpisodeAlertStatus(id, True)
        self.data.reload()

    def searchNewMovies(self):
        self.new_movies = self.searcher_movies.searchUnwatchedMovies()
        for movie in self.new_movies:
            id = self.generateId(movie)
            self.data.putNewMovie(id, False)
            if self.data.getNewMovieAlertStatus(id) is False:
                self.mail.sendmail(self.config.getEmails(),
                                   "[Plex] Un nouveau film est disponible !",
                                   self.mail.getMailNewMovieText(movie),
                                   self.mail.getMailNewMovieHTML(movie))

                self.data.setNewMovieAlertStatus(id, True)
        self.data.reload()


PLEXNOTIFIERS = []


def start():
    config = Configuration(open("config.yml", "r+", encoding='utf-8'))
    plexNotifier = PlexNotifier(Data(open("data.yml", "r+", encoding='utf-8')), config, config.getInstanceName(),
                                config.getInstanceIP(), config.getInstancePort(), config.getInstanceToken())

    PLEXNOTIFIERS.append(plexNotifier)
    plexNotifier.init()


if __name__ == "__main__":
    start()
