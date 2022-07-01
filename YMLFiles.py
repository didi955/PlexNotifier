import yaml
import os


class Configuration:

    """Constructor that loads the configuration file"""
    def __init__(self, file):
        self.file = file
        self.contents = yaml.safe_load(self.file)

    def getSMTPPort(self):
        return self.contents['smtp']['port']

    def getSMTPHost(self):
        return self.contents['smtp']['host']

    def getSMTPMail(self):
        return self.contents['smtp']['mail']

    def getSMTPPassword(self):
        return self.contents['smtp']['password']

    def getInstanceName(self):
        return self.contents['instance']['name']

    def getInstancePort(self):
        return self.contents['instance']['port']

    def getInstanceIP(self):
        return self.contents['instance']['ip']

    def getInstanceToken(self):
        return self.contents['instance']['token']

    def getNameShowsCategory(self):
        return self.contents['categories']['shows']

    def getNameMoviesCategory(self):
        return self.contents['categories']['movies']

    def getEmails(self):
        return self.contents['emails']

    def getTheMovieDBAPIKey(self):
        return self.contents['TheMovieDB']['api_key']

    def getIntervalSeconds(self):
        return self.contents['tasks']['search_new_episodes']['every_seconds']


class Data:

    def __init__(self, file):
        self.file = file
        self.contents = yaml.load(self.file, Loader=yaml.FullLoader)

    def putNewEpisode(self, id: str, status: bool):
        if self.contents['new']['shows']['episodes'] is None:
            self.contents['new']['shows']['episodes'] = {id: {'sent': status}}
        elif id not in self.contents['new']['shows']['episodes']:
            self.contents['new']['shows']['episodes'][id] = {'sent': status}
        elif self.contents['new']['shows']['episodes'][id] is None:
            self.contents['new']['shows']['episodes'][id] = {'sent': status}

    def putNewMovie(self, id: str, status: bool):
        if self.contents['new']['movies'] is None:
            self.contents['new']['movies'] = {id: {'sent': status}}
        elif id not in self.contents['new']['movies']:
            self.contents['new']['movies'][id] = {'sent': status}
        elif self.contents['new']['movies'][id] is None:
            self.contents['new']['movies'][id] = {'sent': status}

    def setNewEpisodeAlertStatus(self, id: str, status: bool):
        self.contents['new']['shows']['episodes'][id]['sent'] = status

    def setNewMovieAlertStatus(self, id: str, status: bool):
        self.contents['new']['movies'][id]['sent'] = status

    def getNewEpisodeAlertStatus(self, id: str):
        return bool(self.contents['new']['shows']['episodes'][id]['sent'])

    def getNewMovieAlertStatus(self, id: str):
        return bool(self.contents['new']['movies'][id]['sent'])

    def isNewEpisodeAlertSendable(self, id: str):
        if self.contents['new']['shows']['episodes'][id]['sent']:
            return True
        else:
            return False

    def isNewMovieAlertSendable(self, id: str):
        if self.contents['new']['movies'][id]['sent']:
            return True
        else:
            return False

    def isUnwatchedEpisodeAlertSendable(self, id: str):
        if self.contents['unwatcheds']['shows']['episodes'][id]['every'] == -1:
            return False
        else:
            return True

    def isUnwatchedMovieAlertSendable(self, id: str):
        if self.contents['unwatcheds']['movies'][id]['every'] == -1:
            return False
        else:
            return True

    def reload(self):
        path = self.file.name
        self.save()
        self.file = open(path, "r+", encoding='utf-8')
        self.contents = yaml.load(self.file, Loader=yaml.FullLoader)

    def save(self):
        path = self.file.name
        self.file.close()
        os.remove(path)
        yaml.dump(self.contents, open(path, "w"))
