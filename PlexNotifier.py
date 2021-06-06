from plexapi.video import Video
from YMLFiles import Configuration
from YMLFiles import Data
from Seacher import SearcherShows
from PlexInstance import PlexInstance
from Mail import Mail
import os
import time


class PlexNotifier:

    @staticmethod
    def generateId(video: Video):
        id = str(video.guid)
        return id

    def __init__(self, data: Data, config: Configuration, name: str, ip: str, port: int, token: str):
        self.config = config
        self.plexinstance = PlexInstance(name, ip, port, token)
        self.data = data
        self.mail = Mail(self.config.getSMTPHost(), self.config.getSMTPPort(),
                         self.config.getSMTPMail(), self.config.getSMTPPassword())
        self.new_episodes = None
        self.searcher = None
        self.shows = None
        self.movies = None

    def init(self):
        self.shows = self.plexinstance.plex.library.section(self.config.getNameShowsCategory())
        self.movies = self.plexinstance.plex.library.section(self.config.getNameMoviesCategory())
        self.searcher = SearcherShows(self.shows)
        self.new_episodes = None
        self.runTask()

    def runTask(self):
        i = 0
        currentTime = time.time()
        while True:
            if i == 0:
                i = 1
                self.searchNewEpisode()
            elif time.time() - currentTime > 61:
                self.searchNewEpisode()
                currentTime = time.time()

    def searchNewEpisode(self):
        self.new_episodes = self.searcher.searchUnwatchedEpisodes()
        for episode in self.new_episodes:
            id = self.generateId(episode)
            self.data.putNewEpisode(id, False)
            if self.data.getNewEpisodeAlertStatus(id) is False:
                nb = episode.index
                show_title = episode.grandparentTitle
                season_nb = episode.parentIndex
                season_title = episode.show().originalTitle
                file_path = episode.media[0].parts[0].file
                poster_path = os.path.dirname(os.path.dirname(file_path))
                html_src = '"' + poster_path + '"'
                self.mail.sendmail(self.config.getEmails(),
                                   "[Plex] Un nouvel épisode est disponible !",
                                   self.mail.getMailNewEpisodeText(season_nb, show_title),
                                   self.mail.getMailNewEpisodeHTML(season_nb, show_title))

                self.data.setNewEpisodeAlertStatus(id, True)
        self.data.reload()


def start():
    config = Configuration(open("config.yml", "r+", encoding='utf-8'))
    plexNotifier = PlexNotifier(Data(open("data.yml", "r+", encoding='utf-8')), config, config.getInstanceName(),
                                config.getInstanceIP(), config.getInstancePort(), config.getInstanceToken())
    plexNotifier.init()


if __name__ == "__main__":
    start()
