import sys
from plexapi.video import Video
from YMLFiles import Configuration
from YMLFiles import Data
from Seacher import SearcherShows
from PlexInstance import PlexInstance
from Mail import Mail
import os
import threading
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

    def start(self):
        self.shows = self.plexinstance.plex.library.section(self.config.getNameShowsCategory())
        self.movies = self.plexinstance.plex.library.section(self.config.getNameMoviesCategory())
        self.searcher = SearcherShows(self.shows)
        self.new_episodes = None
        self.task()

    def task(self):
        self.search_new_Episodes()

    def search_new_Episodes(self):
        self.new_episodes = self.searcher.searchUnwatchedEpisodes()
        current_time = round(time.time())
        while True:
            if current_time - round(time.time()) == int(self.config.contents['tasks']
                                                        ['search_new_episodes']['every_x_seconds']):
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
                        for email in self.config.getEmails():
                            self.mail.sendmail(email,
                                               "[Plex] Un nouvel épisode est disponible !",
                                               self.mail.getMailNewEpisodeText(season_nb, show_title),
                                               self.mail.getMailNewEpisodeHTML(season_nb, show_title))
                        self.data.setNewEpisodeAlertStatus(id, True)

                self.data.save()


def startBackground():
    config = Configuration(open("config.yml", "r+", encoding='utf-8'))
    plexNotifier = PlexNotifier(Data(open("data.yml", "r+", encoding='utf-8')), config, config.getInstanceName(),
                                config.getInstanceIP(), config.getInstancePort(), config.getInstanceToken())
    plexNotifier.start()


if __name__ == "__main__":
    thread = threading.Thread(target=startBackground())
    thread.daemon = True
    thread.start()
    running = True
    while running:
        value = input()
        if value == "stop":
            running = False
            sys.exit()
